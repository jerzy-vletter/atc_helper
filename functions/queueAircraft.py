
from waitingAircraft import populatewindow
from waitingAircraft import to_many_aircraft_warning
from tkinter import messagebox

queued_aircraft = {}
populated = []


def queue_aircraft(name, needs):

    name = name
    needs = needs
    key = len(queued_aircraft)

    if len(queued_aircraft) != 10:
        if key == 0:
            queued_aircraft[key] = [name, needs]
            populated.append(name)
            populatewindow(queued_aircraft)
        else:
            key = len(queued_aircraft)
            if name not in populated:
                queued_aircraft[key] = [name, needs]
                populated.append(name)
                populatewindow(queued_aircraft)
            else:
                messagebox.showinfo("WARNING", "Call-sign already exists")
    else:
        to_many_aircraft_warning()
