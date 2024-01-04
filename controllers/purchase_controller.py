from controllers import event_controller, history_controller
from views.payment_view import PaymentView
from views.ticket_management_view import TicketManagementView

def purchase(event, ticket_type, seat):
    # Process the purchase details
    return PaymentView.display_payment_page(event, ticket_type, seat)


def confirm_purchase(card_number, cvv, event_id, ticket_type, seat):
    if card_number == "1234 5678 9012 3456" and cvv == "789":
        qr_path = "/static/qr-1.svg"
        history_controller.add_to_history(event_id, ticket_type, seat, qr_path)
        return TicketManagementView.display_purchase_confirmation()
    else:
        return PaymentView.display_payment_page(event_controller.get_event(event_id), ticket_type)
