from models.event_model import EventModel
from views.event_view import EventView
from views.event_detail_view import EventDetailView


def get_event(event_id):
    event = EventModel.get_event_by_id(event_id)
    if event:
        return event
    else:
        return "Event not found", 404


def view_events():
    events = EventModel.get_all_events()
    return EventView.display_events(events)


def event_detail(event_id):
    event = EventModel.get_event_by_id(event_id)
    if event:
        return EventDetailView.display_event_detail(event)
    else:
        return "Event not found", 404
