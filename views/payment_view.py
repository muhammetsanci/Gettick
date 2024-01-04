class PaymentView:
    @staticmethod
    def display_payment_page(event, ticket_type, seat):
        display = """
                    <style>
                        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
                        .header { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 20px auto; font-family: 'Montserrat', sans-serif; }
                        .events-title { font-size: 36px; color: #333; }
                        .alt-title { font-size: 22px; color: #333; margin-bottom: 24px; }
                        .ticket-container { max-width: 1200px; margin: auto; font-family: 'Montserrat', sans-serif; }
                        .event-header { display: flex; align-items: center; margin-bottom: 20px; }
                        .event-image { width: 170px; height: 170px; border-radius: 5px; object-fit: cover; margin-right: 20px; }
                        .event-info { flex-grow: 1; }
                        .event-title { font-size: 36px; font-weight: bold; color: #333; }
                        .event-description { font-size: 24px; margin: 5px 0; }
                        .event-details { display: flex; align-items: center; font-size: 18px; margin-top: 5px; }
                        .event-details img { width: 20px; height: 20px; margin-right: 5px; }
                        .divider { border-bottom: 1px solid #ddd; margin: 20px 0; }
                        .form-input { margin-bottom: 10px; width: 50%; padding: 10px; border: 1px solid #ddd; font-size: 14px; border-radius: 20px; box-sizing: border-box; transition: border-color 0.3s; }
                        .form-input:focus { border-color: #007bff; outline: none; }
                        .confirm-purchase-button { width: 50%; padding: 10px; background-color: #007bff; border: none; border-radius: 20px; font-size: 18px; color: white; cursor: pointer; transition: background-color 0.3s; }
                    </style>
                """

        date_icon = '/static/date.png'  # Path to date icon
        time_icon = '/static/time.png'  # Path to time icon
        location_icon = '/static/location.png'  # Path to location icon
        ticket_icon = '/static/ticket.png'  # Path to ticket icon
        seat_icon = '/static/seat.png'  # Path to seat icon

        # Event Header
        display += '<div class="header">'
        display += '<div class="events-title">Make Payment</div>''</div>'
        display += '<div class="ticket-container">'
        display += '<div class="divider"></div>'
        display += '<div class="event-header">'
        display += f'<img src="{event["image_path"]}" alt="{event["name"]}" class="event-image">'
        display += '<div class="event-info">'
        display += f'<div class="event-title">{event["name"]}</div>'
        display += f'<div class="event-description">{event["description"]}</div>'
        display += f'<div class="divider"></div>'
        display += f"""
                        <div class="event-details">
                            <img src="{date_icon}" alt="Date"> {event['date']}
                            <img src="{time_icon}" alt="Time" style="margin-left: 10px;"> {event['time']}
                            <img src="{location_icon}" alt="Location" style="margin-left: 10px;"> {event['venue']}
                            <img src="{ticket_icon}" alt="Price" style="margin-left: 10px;"> {ticket_type}: ${event['price'][ticket_type]}
                            <img src="{seat_icon}" alt="Seat" style="margin-left: 10px;"> {seat}
                        </div>
                    """
        display += '</div>'
        display += '</div>'

        display += f'<div class="divider"></div>'

        display += """
                        <div class="alt-title">Enter Credit/Debit Card Details</div>
                        <form action='/confirm_purchase' method='post'>
                            <div class='credit-card-container'>
                                <input type='text' name='cardNumber' placeholder='Card Number' required class='form-input'>
                                <input type='text' name='cardHolder' placeholder='Card Holder' required class='form-input'>
                                <input type='text' name='expiryDate' placeholder='Expiry Date (MM/YY)' required class='form-input'>
                                <input type='text' name='cvv' placeholder='CVV' required class='form-input'>
                                <input type='hidden' name='eventId' value='{}'>
                                <input type='hidden' name='ticketType' value='{}'>
                                <input type='hidden' name='seat' value='{}'>
                                <button type='submit' class='confirm-purchase-button'>Confirm Purchase</button>
                            </div>
                        </form>    
                """.format(event['id'], ticket_type, seat)

        display += '</div>'
        return display
