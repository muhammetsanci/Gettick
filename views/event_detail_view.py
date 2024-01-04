class EventDetailView:
    @staticmethod
    def display_event_detail(event):
        if not event:
            return "Event not found."

        image_path = event.get('image_path', 'default_image.jpg')

        # Enhanced HTML and CSS for styling
        details = """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
                .detail-container { display: flex; max-width: 1200px; margin: auto; font-family: 'Montserrat', sans-serif; }
                .image-container { flex: 40%; margin-right: 16px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); border-radius: 16px; }
                .info-container { flex: 60%; padding: 20px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); border-radius: 16px;  }
                .info { margin: 10px 0; }
                .info-header { font-size: 36px; font-weight: bold; color: #333; }
                .info-title { font-size: 24px; font-weight: bold; color: #333; }
                .info-content { font-size: 20px; }
                .divider { border-bottom: 1px solid #ddd; margin: 30px 0; }
                .button { background-color: #007bff; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 20px 0; cursor: pointer; border-radius: 5px; transition: background-color 0.3s ease; }
                .button:hover { background-color: #0056b3; }
                img { width: auto; height: 100%; max-height: 650px; border-radius: 16px; }
                ul { padding: 0; }
                li { list-style: none; padding: 5px 0; }
            </style>
        """

        details += f"""
            <div class="detail-container">
                <div class="image-container">
                    <img src="{image_path}" alt="{event['name']}">
                </div>
                <div class="info-container">
                    <div class="info">
                        <div class="info-header">{event['name']}</div>
                    </div>
                    <div class="info">
                        <div class="info-content">{event['description']}</div>
                    </div>
                    <div class="divider"></div>
                    <div class="info"><span class="info-title">Date:</span> <span class="info-content">{event['date']}</span></div>
                    <div class="info"><span class="info-title">Time:</span> <span class="info-content">{event['time']}</span></div>
                    <div class="info"><span class="info-title">Venue:</span> <span class="info-content">{event['venue']}</span></div>
                    <div class="info"><span class="info-title">Rules:</span> <span class="info-content">{event['rules']}</span></div>
                    <div class="divider"></div>
                    <div class="info">
                        <div class="info-title">Ticket Types</div>
                        <div class="info-content">{EventDetailView.format_ticket_types(event['price'])}</div>
                    </div>
                    <a href="/purchase_ticket/{event['id']}" class="button">Purchase Tickets</a>
                </div>
            </div>
        """
        return details

    @staticmethod
    def format_ticket_types(ticket_types):
        formatted = "<ul>"
        for type, price in ticket_types.items():
            formatted += f"<li><strong>{type}:</strong> ${price}</li>"
        formatted += "</ul>"
        return formatted
