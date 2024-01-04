class EventView:
    @staticmethod
    def display_events(events):
        if not events:
            return "No events available."

        display = """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
                .header { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 20px auto; font-family: 'Montserrat', sans-serif; }
                .events-title { font-size: 36px; color: #333; }
                .search-container { display: flex; align-items: center; }
                .search-bar { padding: 10px; padding-left: 15px; border: 1px solid #ddd; border-radius: 20px; height: 40px; width: 400px; font-family: 'Montserrat', sans-serif; font-size: 14px; }
                .search-button { background-color: #FFFFFF; border: 1px solid #ddd; margin-left: 10px; border-radius: 20px; height: 40px; width: 40px; }
                .search-button:hover {background-color: #ededed; }
                .search-button img { width: 18px; height: 18px; }
                .history-button { background-color: #FFFFFF; border: 1px solid #ddd; margin-left: 10px; border-radius: 20px; height: 40px; width: 110px; font-family: 'Montserrat', sans-serif; font-size: 14px; transition: background-color 0.3s, color 0.3s; }
                .history-button:hover {background-color: #ededed; }
                .events-list { max-width: 1200px; margin: auto; font-family: 'Montserrat', sans-serif; }
                .event-container { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 10px; display: flex; align-items: start; }
                .image { width: 120px; height: 120px; border-radius: 10px; margin-right: 20px; object-fit: cover; }
                .divider { border-bottom: 1px solid #ddd; margin: 20px 0; }
                .event-info { flex-grow: 1; }
                .event-title { font-size: 20px; font-weight: bold; color: #333; margin: 0; }
                .event-description { font-size: 16px; margin: 5px 0; }
                .event-details { display: flex; align-items: center; font-size: 14px; margin-top: 5px; }
                .event-details img { width: 16px; height: 16px; margin-right: 5px; }
                a { text-decoration: none; color: inherit; }
            </style>
        """

        # Header with title and search bar
        display += '<div class="header">'
        display += '<div class="events-title">Events</div>'
        display += '<div class="search-container">'
        display += '<input type="text" class="search-bar" placeholder="search for the best event in the town">'
        search_icon_path = '/static/search.png'
        display += f'<button class="search-button" title="NOT IMPLEMENTED YET"><img src="{search_icon_path}" alt="Search Icon"></button>'
        filter_icon_path = '/static/filter.png'
        display += f'<button class="search-button" title="NOT IMPLEMENTED YET"><img src="{filter_icon_path}" alt="Search Icon"></button>'
        display += '</div>'
        display += f"""<button class="history-button" onclick="window.location.href='/my-events'">My Events</button>"""
        display += '</div>'

        # Events list
        display += '<div class="events-list">'
        for event in events:
            event_link = f"/event/{event['id']}"
            image_path = event.get('image_path', 'default_image.jpg')
            date_icon = '/static/date.png'  # Path to date icon
            time_icon = '/static/time.png'  # Path to time icon
            location_icon = '/static/location.png'  # Path to location icon

            display += f"""
                <a href="{event_link}">
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
                            </div>
                        </div>
                    </div>
                </a>
            """
        display += '</div>'
        return display
