from flask import Flask, request
from controllers import login_controller, event_controller, ticket_controller, purchase_controller, history_controller

app = Flask(__name__)


@app.route('/', methods=['GET'])
def login_page():
    return login_controller.login_page()


@app.route('/login', methods=['POST'])
def login():
    # Extract username and password from form data
    username = request.form['username']
    password = request.form['password']
    return login_controller.login(username, password)


@app.route('/event')
def view_events():
    return event_controller.view_events()


@app.route('/event/<int:event_id>')
def event_detail(event_id):
    return event_controller.event_detail(event_id)


@app.route('/purchase_ticket/<int:event_id>', methods=['GET'])
def purchase_ticket(event_id):
    return ticket_controller.purchase_ticket(event_id)


@app.route('/purchase', methods=['POST', 'GET'])
def process_purchase():
    event_id = int(request.form['eventId'])
    seat = request.form['selectedSeat']
    ticket_type = request.form['ticketType']

    return purchase_controller.purchase(event_controller.get_event(event_id), ticket_type, seat)


@app.route('/confirm_purchase', methods=['POST'])
def confirm_purchase():
    card_number = request.form['cardNumber']
    cvv = request.form['cvv']
    event_id = int(request.form['eventId'])
    ticket_type = request.form['ticketType']
    seat = request.form['seat']

    return purchase_controller.confirm_purchase(card_number, cvv, event_id, ticket_type, seat)


@app.route('/my-events')
def view_my_events():
    return history_controller.view_my_events()


@app.route('/preview-qr', methods=['POST'])
def view_qr_code():
    qr_path = request.form['qrPath']
    return history_controller.view_qr_code(qr_path)


if __name__ == '__main__':
    app.run(debug=True)
