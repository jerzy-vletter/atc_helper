
from waitingAircraft import populatewindow

queued_aircraft = {}


def queue_aircraft(name, a_type, needs):

    name = name
    a_type = a_type
    needs = needs
    key = len(queued_aircraft)

    if key == 0:
        queued_aircraft[key] = [name, a_type, needs]
        populatewindow(queued_aircraft)
    else:
        key = len(queued_aircraft)
        queued_aircraft[key] = [name, a_type, needs]
        populatewindow(queued_aircraft)
