class LoginModel:
    _users = [
        {"username": "user1", "password": "pass1"},
        {"username": "user2", "password": "pass2"},
        {"username": "group04", "password": "softeng"}
    ]

    @classmethod
    def get_user_by_username(cls, username):
        return next((user for user in cls._users if user['username'] == username), None)
