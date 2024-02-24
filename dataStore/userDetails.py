
from edge_cases import ( InvalidUser,  UserAlreadyExists)


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.name in self.users:
            raise UserAlreadyExists()
        self.users[user.name] = user

    def get_user(self, user_name):
        if user_name not in self.users:
            raise InvalidUser()
        return self.users[user_name]

    def get_users(self):
        return self.users.values()
