from models.history_model import HistoryModel
from models.event_model import EventModel
from views.qr_view import QRView
from views.history_view import HistoryView


def view_my_events():
    history = HistoryModel.get_all_history()
    return HistoryView.display_my_events(history)


def view_qr_code(qr_path):
    return QRView.display_qr(qr_path)


def add_to_history(event_id, ticket_type, seat, qr_path):
    purchased_event = EventModel.get_event_by_id(event_id)
    purchased_event.update({"ticket_type": ticket_type})
    purchased_event.update({"seat": seat})
    purchased_event.update({"qr_path": qr_path})
    print(purchased_event)
    HistoryModel.history.append(purchased_event)
