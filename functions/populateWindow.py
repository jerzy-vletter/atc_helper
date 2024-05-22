
from window.CreateQueueWindow import CreateQueueWindow
from tkinter import *
from tkinter import messagebox

populated = []


def populatewindow(queued_aircraft: dict, window_needed: bool):

    queued_aircraft = queued_aircraft
    window_needed = window_needed

    if window_needed:
        queue_window = CreateQueueWindow()
    else:
        pass

    for i in range(len(queued_aircraft)):

        name = queued_aircraft[i][0]
        a_type = queued_aircraft[i][1]
        needs = queued_aircraft[i][2]

        if name not in populated:
            label_var = StringVar()
            populate = Label(queue_window, textvariable=label_var)
            label_var.set(name + " needs: " + needs)

            populated.append(name)
            populate.pack()
        else:
            pass


