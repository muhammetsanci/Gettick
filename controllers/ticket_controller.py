from models.event_model import EventModel
from views.ticket_purchase_view import TicketPurchaseView


def purchase_ticket(event_id):
    event = EventModel.get_tickets_for_event(event_id)
    return TicketPurchaseView.display_ticket_options(event)
