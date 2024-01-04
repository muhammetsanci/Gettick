class HistoryView:
    @staticmethod
    def display_my_events(history):
        display = """
                    <style>
                        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
                        .header { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 20px auto; font-family: 'Montserrat', sans-serif; }
                        .events-title { font-size: 36px; color: #333; }
                        .warning { font-family: 'Montserrat', sans-serif; font-size: 20px }
                        .search-container { display: flex; align-items: center; }
                        .events-list { max-width: 1200px; margin: auto; font-family: 'Montserrat', sans-serif; }
                        .event-container { display: flex; border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 10px;  }
                        .image { width: 120px; height: 120px; border-radius: 10px; margin-right: 20px; object-fit: cover; }
                        .divider { border-bottom: 1px solid #ddd; margin: 20px 0; }
                        .event-info { flex-grow: 0.80; }
                        .operation-info { flex-grow: 0.20; display: flex; margin-left: 50px; flex-direction: column; align-items: flex-start; }
                        .cancel-button { background-color: #D81616; color: white; margin: 10px; margin-bottom: 0px; border: none; border-radius: 20px; height: 40px; width: 125px; font-family: 'Montserrat', sans-serif; font-size: 14px; }
                        .cancel-button:hover {background-color: #DB2626; }
                        .preview-button { background-color: #FFFFFF; color: black; margin: 10px; margin-bottom: 0px; border: 1px solid #ddd; border-radius: 20px; height: 40px; width: 125px; font-family: 'Montserrat', sans-serif; font-size: 14px; }
                        .preview-button:hover {background-color: #ededed; }
                        .event-title { font-size: 20px; font-weight: bold; color: #333; margin: 0; }
                        .event-description { font-size: 16px; margin: 5px 0; }
                        .event-details { display: flex; align-items: center; font-size: 14px; margin-top: 5px; }
                        .event-details img { width: 16px; height: 16px; margin-right: 5px; }
                        a { text-decoration: none; color: inherit; }
                    </style>
                """

        # Header with title and search bar
        display += '<div class="header">'
        display += '<div class="events-title">My Events</div>'
        display += '</div>'

        # Events list
        display += '<div class="events-list">'

        if not history:
            display += """<div class="divider"></div>"""
            display += """<div class="warning">Your history is empty. Time to create some memories!</div>"""

        for event in history:
            image_path = event.get('image_path', 'default_image.jpg')
            qr_path = event.get('qr_path', 'default_image.jpg')
            date_icon = '/static/date.png'  # Path to date icon
            time_icon = '/static/time.png'  # Path to time icon
            location_icon = '/static/location.png'  # Path to location icon
            ticket_icon = '/static/ticket.png'  # Path to ticket icon
            seat_icon = '/static/seat.png'  # Path to seat icon

            display += f"""
                            <div class="event-container">
                                <img src="{image_path}" alt="{event['name']}" class="image">
                                <div class="event-info">
                                    <p class="event-title">{event['name']}</p>
                                    <p class="event-description">{event['description']}</p>
                                    <div class="divider"></div>
                                    <div class="event-details">
                                        <img src="{date_icon}" alt="Date"> {event['date']}
                                        <img src="{time_icon}" alt="Time" style="margin-left: 10px;"> {event['time']}
                                        <img src="{location_icon}" alt="Location" style="margin-left: 10px;"> {event['venue']}
                                        <img src="{ticket_icon}" alt="Price" style="margin-left: 10px;"> {event['ticket_type']}: ${event['price'][event['ticket_type']]}
                                        <img src="{seat_icon}" alt="Seat" style="margin-left: 10px;"> {event['seat']}
                                    </div>
                                </div>
                                <div class="operation-info">
                                    <button class="cancel-button" title="NOT IMPLEMENTED YET">Cancel</button>
                                    <form action="/preview-qr" method="post">
                                        <input type="hidden" name="qrPath" value="{qr_path}">
                                        <button type="submit" class="preview-button">Preview QR</button>
                                    </form>
                                </div>
                            </div>
                    """
        display += '</div>'
        return display
