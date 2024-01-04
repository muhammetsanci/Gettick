from models.event_model import EventModel
from models.login_model import LoginModel
from views.login_view import LoginView
from views.event_view import EventView


def login_page():
    return LoginView.display_login_form()


def login(username, password):
    user = LoginModel.get_user_by_username(username)
    if user and user["password"] == password:
        events = EventModel.get_all_events()
        return EventView.display_events(events)
    else:
        return LoginView.display_login_form()
