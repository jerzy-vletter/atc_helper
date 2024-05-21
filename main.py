# atc_helper, keep track of stuf.

import tkinter
from window.CreateMainWindow import CreateMainWindow

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # create the main window where we add all the strips.
    add_aircraft_window = CreateMainWindow()

    # title text
    label_var = tkinter.StringVar()
    add_strip_label = tkinter.Label(add_aircraft_window, textvariable=label_var, font='bold')
    label_var.set("ADD STRIP HERE")

    # input fields
    label_var = tkinter.StringVar()
    aircraft_name_label = tkinter.Label(add_aircraft_window, textvariable=label_var, font='bold')
    label_var.set("define: call sign")

    aircraft_name = tkinter.Entry(add_aircraft_window)
    aircraft_name.insert(0, 'call sign')

    # packing all the entities (add pady=5 for vertical separation after the first one)
    add_strip_label.pack()
    aircraft_name_label.pack()
    aircraft_name.pack()

    # running the main loop, keep everything inside here
    add_aircraft_window.mainloop()
