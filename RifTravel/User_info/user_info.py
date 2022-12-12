from Route_info import route_info
from datetime import datetime

class User:
    def __init__(self, name: str, email: str, password: str, age: int):
        self.name = name
        self.email = email
        self.password = password
        self.age = age

    def register(self):
        pass

    def login(self):
        pass

    def edit_profile(self):
        return User()

    def delete_account(self):
        pass


class RouteAuthor(User):
    def __init__(self, name: str, email: str, password: str, age: int, shared_route_counter: int):
        super().__init__(name, email, password, age)
        self.shared_route_coutner = shared_route_counter

    def remove_shared_route(self, route: route_info.Route):
        pass


class Group:
    def __init__(self, member_count: int, ability: str):
        self.people_count = member_count
        self.ability = ability
        self.created_at = datetime.datetime.now()

    def add_user(self, user: User):
        pass

    def remove_user(self, user: User):
        pass

    def create_group(self):
        pass