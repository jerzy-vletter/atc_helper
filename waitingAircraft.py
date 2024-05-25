
from window.CreateQueueWindow import CreateQueueWindow
from tkinter import *
from tkinter import messagebox  # type: ignore

populated = []

window_exists = False


# noinspection PyGlobalUndefined
def reloadwindow(exists: bool, queued_aircraft):  # Rename the parameter
    global window_exists  # Explicitly reference the global variable
    global queue_window
    if not exists:
        queue_window = CreateQueueWindow()
        window_exists = True
        return queue_window
    else:
        queue_window.destroy()
        queue_window = CreateQueueWindow()
        repopulate(populated, queued_aircraft)
        return queue_window


def populatewindow(queued_aircraft: dict):
    queued_aircraft = queued_aircraft

    queue_window = reloadwindow(window_exists, queued_aircraft)

    queue_window.columnconfigure((0, 1, 2, 3), weight=1)
    queue_window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    for i in range(len(queued_aircraft)):

        name = queued_aircraft[i][0]
        a_type = queued_aircraft[i][1]
        needs = queued_aircraft[i][2]

        key = i

        if name not in populated:

            label_var = StringVar()
            populate_name = Label(queue_window, textvariable=label_var)
            label_var.set("aircraft: " + name)

            label_var = StringVar()
            populate_type = Label(queue_window, textvariable=label_var)
            label_var.set("type: " + a_type)

            label_var = StringVar()
            populate_needs = Label(queue_window, textvariable=label_var)
            label_var.set("needs: " + needs)

            button_text = StringVar()
            button_text.set("X")
            del_button = Button(queue_window, textvariable=button_text,
                                command=lambda: delete_aircraft(name, populated, queued_aircraft, key))

            populate_name.grid(row=i, column=0, sticky='w')
            populate_type.grid(row=i, column=1, sticky='w')
            populate_needs.grid(row=i, column=2, sticky='w')
            del_button.grid(row=i, column=3, sticky='w')

            populated.append(name)
        else:
            pass


def repopulate(populated: list, queued_aircraft):
    queue_window.columnconfigure((0, 1, 2, 3), weight=1)
    queue_window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    for i in range(len(populated)):

        name = queued_aircraft[i][0]
        a_type = queued_aircraft[i][1]
        needs = queued_aircraft[i][2]

        key = i

        label_var = StringVar()
        populate_name = Label(queue_window, textvariable=label_var)
        label_var.set("aircraft: " + name)

        label_var = StringVar()
        populate_type = Label(queue_window, textvariable=label_var)
        label_var.set("type: " + a_type)

        label_var = StringVar()
        populate_needs = Label(queue_window, textvariable=label_var)
        label_var.set("needs: " + needs)

        button_text = StringVar()
        button_text.set("X")
        del_button = Button(queue_window, textvariable=button_text,
                            command=lambda: delete_aircraft(name, populated, queued_aircraft, key))

        populate_name.grid(row=i, column=0, sticky='w')
        populate_type.grid(row=i, column=1, sticky='w')
        populate_needs.grid(row=i, column=2, sticky='w')
        del_button.grid(row=i, column=3, sticky='w')

        if name not in populated:
            populated.append(name)
        else:
            pass


def delete_aircraft(name, populated, queued_aircraft, key):
    populated.remove(name)
    queued_aircraft.pop(key)
    reloadwindow(window_exists, queued_aircraft)
