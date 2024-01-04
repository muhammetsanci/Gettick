class TicketPurchaseView:
    @staticmethod
    def display_ticket_options(event):
        display = """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
                .header { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 20px auto; font-family: 'Montserrat', sans-serif; }
                .events-title { font-size: 36px; color: #333; }
                .ticket-container { max-width: 1200px; margin: auto; font-family: 'Montserrat', sans-serif; }
                .main-container { display: flex; }
                .ticket-options { flex: 1; margin-right: 30px; }
                .seating { flex: 1; }
                .event-header { display: flex; align-items: center; margin-bottom: 20px; }
                .event-image { width: 170px; height: 170px; border-radius: 5px; object-fit: cover; margin-right: 20px; }
                .event-info { flex-grow: 1; }
                .event-title { font-size: 36px; font-weight: bold; color: #333; }
                .event-description { font-size: 24px; margin: 5px 0; }
                .event-details { display: flex; align-items: center; font-size: 18px; margin-top: 5px; }
                .event-details img { width: 20px; height: 20px; margin-right: 5px; }
                .divider { border-bottom: 1px solid #ddd; margin: 20px 0; }
                .ticket { cursor: pointer; margin-bottom: 10px; padding: 10px; border: 1px solid #ddd; height: 82px; border-radius: 10px; transition: all 0.3s; }
                .ticket:hover, .ticket.selected { border-color: #007bff; background-color: #f0f8ff; }"
                .ticket-title { font-size: 24px; font-weight: bold; color: #007bff; margin: 0; }
                .ticket-price { font-size: 20px; margin: 5px 0; }
                .purchase-button { width: 49%; padding: 10px; background-color: #007bff; border: none; border-radius: 20px; font-size: 18px; color: white; cursor: pointer; transition: background-color 0.3s; }
                .selected { background-color: red; }
                .button { 
                        background-color: #FFFFFF; 
                        border: 1px solid #ddd; 
                        margin: 2px; 
                        border-radius: 10px; 
                        height: 40px; 
                        width: 40px; 
                }
                .button:hover { 
                        background-color: #EDEDED; 
                        border: 2px solid #ddd;
                        margin: 1px;  
                        height: 42px; 
                        width: 42px; 
                }
                .button.selected { 
                        border-color: #007bff; background-color: #f0f8ff;
                 }
            </style>

            <script>
                function selectTicketType(ticketType) {
                    // Deselect all tickets
                    document.querySelectorAll('.ticket').forEach(ticket => {
                        ticket.classList.remove('selected');
                    });
                    // Select the clicked ticket
                    document.getElementById('ticket-' + ticketType).classList.add('selected');
                    // Set the value for the hidden input
                    document.getElementById('selectedTicketType').value = ticketType;
                }
            </script>

            <script>
                var selectedSeat = '';

                function selectSeat(seatId) {
                    // Logic to handle seat selection
                    var currentSelected = document.querySelector('.selected');

                    document.querySelectorAll('.button').forEach(seat => {
                        seat.classList.remove('selected');
                    });
                
                    var seatElement = document.getElementById('seat-' + seatId);
                    if (seatElement) {
                        seatElement.classList.add('selected');
                        selectedSeat = seatId;
                        document.getElementById('selectedSeat').value = seatId;
                    }
                }
            </script>

        """

        date_icon = '/static/date.png'  # Path to date icon
        time_icon = '/static/time.png'  # Path to time icon
        location_icon = '/static/location.png'  # Path to location icon

        # Event Header
        display += '<div class="header">'
        display += '<div class="events-title">Choose Ticket Type</div>''</div>'
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
                        </div>
                    """
        display += '</div>'
        display += '</div>'

        display += f'<div class="divider"></div>'

        # Main container
        display += '<div class="main-container">'
        display += '<div class="ticket-options">'

        # Ticket options
        for ticket_type, price in event["price"].items():
            display += f"""
                        <div class="ticket" id="ticket-{ticket_type}" onclick="selectTicketType('{ticket_type}')">
                            <div class="ticket-title">{ticket_type} Ticket</div>
                            <div class="ticket-price">${price}</div>
                        </div>
                    """

        display += '</div>'  # Closing ticket-options div

        # Placeholder for seating
        display += '<div class="seating">'
        display += f"""
                    <div id="seating-chart"></div>
                    <script>
                        function getRowLetter(rowNumber) {{
                            return String.fromCharCode('A'.charCodeAt(0) + rowNumber);
                        }}

                        for (let i = 0; i < 5; i++) {{
                            for (let j = 0; j < 13; j++) {{
                                let seat = document.createElement('button');
                                seat.className = 'button';
                                let rowLetter = getRowLetter(i);
                                seat.innerText = rowLetter + '-' + (j + 1);
                                let seatId = rowLetter + '-' + (j + 1);
                                seat.onclick = function() {{ selectSeat(rowLetter + '-' + (j + 1)); }};
                                document.getElementById('seating-chart').appendChild(seat);

                                seat.id = 'seat-' + seatId;  // Assign an ID to each seat
                                seat.onclick = function() {{ selectSeat(seatId); }};
                            }}
                            document.getElementById('seating-chart').appendChild(document.createElement('br'));
                        }}
                    </script>
                    """
        display += '</div>'  # Closing seating-container div

        display += '</div>'  # Closing main-container div

        # Purchase button and hidden input for selected ticket type
        display += """
                    <form action="/purchase" method="post">
                        <input type="hidden" id="selectedTicketType" name="ticketType" value="">
                        <input type="hidden" name="eventId" value="{}">
                        <input type="hidden" id="selectedSeat" name="selectedSeat" value="">
                        <button type="submit" class="purchase-button">Purchase</button>
                    </form>
                """.format(event['id'])

        return display
