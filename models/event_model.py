class EventModel:
    _events = [
        {
            "id": 1,
            "name": "Pink Floyd",
            "description": "The sun is the same, in relative way, but you're older...",
            "date": "2024-02-15",
            "time": "19:00",
            "venue": "City Arena",
            "price": {"Standard": 50, "VIP": 100},
            "rules": "Bring ID for registration.",
            "image_path": "/static/pink-floyd.png"
        },
        {
            "id": 2,
            "name": "Metallica",
            "description": "Because you're unforgiven too!",
            "date": "2024-05-25",
            "time": "18:00",
            "venue": "Wesley Stadium",
            "price": {"Standard": 200, "VIP": 350},
            "rules": "Bring ID for registration.",
            "image_path": "/static/metallica.png"
        },
        {
            "id": 3,
            "name": "Guns n' Roses",
            "description": "Don't you cry, tonight, I still love you baby!",
            "date": "2024-08-20",
            "time": "17:00",
            "venue": "City Arena",
            "price": {"Standard": 250, "VIP": 450},
            "rules": "Bring ID for registration.",
            "image_path": "/static/guns-n-roses.png"
        },
        {
            "id": 4,
            "name": "The Doors",
            "description": "Like a dog without a bone, an actor out on loan, riders on the storm...",
            "date": "2024-03-20",
            "time": "20:00",
            "venue": "Wesley Stadium",
            "price": {"Standard": 300, "VIP": 500},
            "rules": "Bring ID for registration.",
            "image_path": "/static/the-doors.png"
        }
    ]

    @classmethod
    def get_all_events(cls):
        return cls._events

    @classmethod
    def get_event_by_id(cls, event_id):
        return next((event for event in cls._events if event['id'] == event_id), None)

    @classmethod
    def get_tickets_for_event(cls, event_id):
        return next((event for event in cls._events if event['id'] == event_id), None)
