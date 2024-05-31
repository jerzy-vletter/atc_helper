
from window.CreateQueueWindow import CreateQueueWindow
from tkinter import *
from tkinter import messagebox  # type: ignore

"""
explanation time, this variable needs to exist on a global level to prevent warnings, it doesn't have to do anything yet
warning in question: queue_window doesn't get assigned at module level, because it gets assigned in a if statement.
"""
queue_window = ...

populated = []
window_exists = False
grid_col = 5
grid_row = 10


def reloadwindow(exists: bool, queued_aircraft):
    global window_exists
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

    counter = 0

    queue_window = reloadwindow(window_exists, queued_aircraft)

    for c in range(grid_col):
        queue_window.columnconfigure(index=c, weight=1)
    for r in range(grid_row):
        queue_window.rowconfigure(index=r, weight=1)

    for i in range(len(queued_aircraft)):

        name = queued_aircraft[i][0]
        a_type = queued_aircraft[i][1]
        needs = queued_aircraft[i][2]

        key = i

        if name not in populated:

            name = queued_aircraft[key][0]
            a_type = queued_aircraft[key][1]
            needs = queued_aircraft[key][2]

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
                                command=lambda n=name, k=key: delete_aircraft(n, populated, queued_aircraft, k))

            update_text = StringVar()
            update_text.set("update")
            update_button = Button(queue_window, textvariable=update_text,
                                   command=lambda n=name, a=a_type, ne=needs, k=key:
                                   update_aircraft(n, a, ne, k, queued_aircraft))

            populate_name.grid(row=counter, column=0, sticky='w')
            populate_type.grid(row=counter, column=1, sticky='w')
            populate_needs.grid(row=counter, column=2, sticky='w')
            del_button.grid(row=counter, column=3, sticky='w')
            update_button.grid(row=counter, column=4, sticky='w')

            counter += 1

            populated.append(name)
        else:
            pass


def repopulate(populated: list, queued_aircraft: dict):
    counter = 0

    for c in range(grid_col):
        queue_window.columnconfigure(index=c, weight=1)
    for r in range(grid_row):
        queue_window.rowconfigure(index=r, weight=1)

    keys = queued_aircraft.keys()

    for key in keys:

        name = queued_aircraft[key][0]
        a_type = queued_aircraft[key][1]
        needs = queued_aircraft[key][2]

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
                            command=lambda n=name, k=key: delete_aircraft(n, populated, queued_aircraft, k))

        update_text = StringVar()
        update_text.set("update")
        update_button = Button(queue_window, textvariable=update_text,
                               command=lambda n=name, a=a_type, ne=needs, k=key:
                               update_aircraft(n, a, ne, k, queued_aircraft))

        populate_name.grid(row=counter, column=0, sticky='w')
        populate_type.grid(row=counter, column=1, sticky='w')
        populate_needs.grid(row=counter, column=2, sticky='w')
        del_button.grid(row=counter, column=3, sticky='w')
        update_button.grid(row=counter, column=4, sticky='w')

        counter += 1

        if name not in populated:
            populated.append(name)
        else:
            pass


def delete_aircraft(name, populated, queued_aircraft, key):

    populated.remove(name)
    queued_aircraft.pop(key)
    reloadwindow(window_exists, queued_aircraft)


def update_aircraft(name, a_type, needs, key, queued_aircraft):

    valid_needs = ['clearance', 'pushback', 'taxi']
    if needs in valid_needs:
        index = valid_needs.index(needs)
        if index < len(valid_needs) - 1:
            new_needs = valid_needs[index + 1]
            queued_aircraft.update({key: [name, a_type, new_needs]})
            reloadwindow(window_exists, queued_aircraft)
        else:
            delete_aircraft(name, populated, queued_aircraft, key)
    else:
        messagebox.showinfo("WARNING", "i don't know how, but " + name +
                            " needs something that wasn't programmed, pls contact the creator")


def to_many_aircraft_warning():
    messagebox.showinfo("WARNING", "You already have 10 aircraft waiting for something, go clean those up")
