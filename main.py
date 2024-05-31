# atc_helper, keep track of stuf.

from tkinter import *
from tkinter import messagebox
from window.CreateMainWindow import CreateMainWindow
from functions.queueAircraft import queue_aircraft


def push_aircraft(needs_list):
    valid_needs = needs_list

    name = aircraft_name_field.get()
    a_type = aircraft_type_field.get()
    needs = format(aircraft_needs.get())

    if needs not in valid_needs:
        messagebox.showinfo("WARNING", "i don't know how, but you broke the selection list...")
    else:
        queue_aircraft(name, a_type, needs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # create the main window where we add all the strips.
    add_aircraft_window = CreateMainWindow()

    # title text
    label_var = StringVar()
    add_strip_label = Label(add_aircraft_window, textvariable=label_var, font='bold')
    label_var.set("ADD STRIP HERE")

    # input fields | names
    label_var = StringVar()
    aircraft_name_label = Label(add_aircraft_window, textvariable=label_var, font='bold')
    label_var.set("aircraft call sign:")

    label_var = StringVar()
    aircraft_type_label = Label(add_aircraft_window, textvariable=label_var, font='bold')
    label_var.set("aircraft type:")

    label_var = StringVar()
    aircraft_need_label = Label(add_aircraft_window, textvariable=label_var, font='bold')
    label_var.set("aircraft needs:")

    # input fields | logic (for buttons / OptionMenus / etc.)
    aircraft_needs = StringVar()
    aircraft_needs.set("clearance")
    needs_list = ['clearance', 'pushback', 'taxi', 'takeoff']

    button_text = StringVar()
    button_text.set("submit aircraft")

    # input fields | fields
    aircraft_name_field = Entry(add_aircraft_window)
    aircraft_type_field = Entry(add_aircraft_window)
    aircraft_need_field = OptionMenu(add_aircraft_window, aircraft_needs, *needs_list)

    # submit button
    submit_button = Button(add_aircraft_window, textvariable=button_text, command=lambda: push_aircraft(needs_list))

    # defining the grid
    add_aircraft_window.columnconfigure((0, 1, 2), weight=1)
    add_aircraft_window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # placing everything on the window
    add_strip_label.grid(row=0, column=1, sticky='w')

    aircraft_name_label.grid(row=1, column=0, sticky='snew')
    aircraft_name_field.grid(row=1, column=1, sticky='w')
    aircraft_type_label.grid(row=2, column=0, sticky='snew')
    aircraft_type_field.grid(row=2, column=1, sticky='w')
    aircraft_need_label.grid(row=3, column=0, sticky='snew')
    aircraft_need_field.grid(row=3, column=1, sticky='w')
    submit_button.grid(row=4, column=1, sticky='snew')

    # running the main loop, keep everything inside here
    add_aircraft_window.mainloop()
