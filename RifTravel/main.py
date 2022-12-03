# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime
from abc import ABC, abstractmethod


def parse_data():
    route_data = []
    with open("route_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            route_data.append(line.strip())
    temp = []
    final = []
    for data in route_data:
        if data == "":
            final.append(temp)
            temp = []
        else:
            temp.append(data)
    return final


class Booking(ABC):

    @abstractmethod
    def book(self):
        pass


class Weather:
    def __init__(self, location: str, state: str, temperature: int, time: datetime):
        self.location = location
        self.state = state
        self.temperature = temperature
        self.time = time


class Location:
    def __init__(self, latitude: str, longitude: str, time_zone: str, country: str):
        self.latitude = latitude
        self.longitude = longitude
        self.time_zone = time_zone
        self.country = country


class Rating:
    def __init__(self, rating: int, comment: str):
        self.rating = rating
        self.comment = comment

    def create_rating(self, route, user):
        return Rating

    def remove_rating(self, route, user):
        pass

    def publish_rating(self):
        return Rating

    def edit_rating(self):
        return Rating


class Activity(Booking):
    def __init__(self, min_age: int, type: str, price: int, rating: Rating):
        self.min_age = min_age
        self.type = type
        self.price = price
        self.rating = rating

    def book(self):
        pass


class Stop:
    def __int__(self, rating: Rating, type: str, price: int):
        self.rating = rating
        self.type = type
        self.price = price


class Accomodation(Stop, Booking):
    def __init__(self, rating: Rating, type: str, price: int, accomodation_type: str):
        super().__init__(rating, type, price)
        self.accomodation_type = accomodation_type

    def book(self):
        pass


class Route:
    def __init__(self, start: str, end: str, length: int, severity: int, activities: list, stops: list,
                 weather: Weather, rating: Rating):
        self.start = start
        self.end = end
        self.length = length
        self.severity = severity
        self.activities = activities
        self.stops = stops
        self.weather = weather
        self.rating = rating

    def save_route(self):
        return Route

    def add_activities(self, activity: Activity):
        self.activities.append(activity)
        return Route

    def add_stops(self, stop: Stop):
        self.stops.append(stop)
        return Route

    def edit_route(self):
        return Route

    def download_route(self):
        return Route

    def delete_route(self):
        pass

    def accept_route(self):
        pass


class SavedRoute(Route):
    def __init__(self, start: str, end: str, length: int, severity: int, activities: list, stops: list,
                 weather: Weather, rating: Rating, date: datetime):
        super().__init__(start, end, length, severity, activities, stops, weather, rating)
        self.date = date


class User:
    def __init__(self, name: str, email: str, password: str, age: int, rating: int, friends):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.rating = rating
        self.friends = friends
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def register(self):
        pass

    def login(self):
        pass

    def create_group(self):
        return Group()

    def share_route(saved_route: SavedRoute):
        pass

    def create_route(self):
        route_details = parse_data()

        activities = route_details[0]
        severity = int(route_details[1][0])
        travelling_as = route_details[2][0]
        sleeping = route_details[2][1]
        start_location = route_details[3][0]
        end_location = route_details[3][1]
        date = route_details[4][0]

        print(activities, severity, travelling_as, sleeping, start_location, end_location, date)

        if len(activities) > 5:
            return False

        print(route_details)

        #return Route()

    def edit_profile(self):
        return User()

    def delete_account(self):
        pass

user = User("John John", "john@gmail.com", "123456", 20, 5, None)
user.create_route()



class RouteAuthor(User):
    def __init__(self, name: str, email: str, password: str, age: int, rating: int, friends, shared_route_counter: int):
        super().__init__(name, email, password, age, rating, friends)
        self.shared_route_coutner = shared_route_counter

    def remove_shared_route(self, route: Route):
        pass


class Group:
    def __init__(self, people_count: int, ability: str):
        self.people_count = people_count
        self.ability = ability
        self.created_at = datetime.datetime.now()

    def add_user(self, user: User):
        pass

    def remove_user(self, user: User):
        pass


class Invite:
    def __init__(self, date: datetime, state: str, sender: User, receiver: User):
        self.date = date
        self.state = state
        self.sender = sender
        self.receiver = receiver

    def accept(self):
        self.state = 'accepted'

    def reject(self):
        self.state = 'rejected'

    def create_invite(self, sender: User, receiver: User):
        self.sender = sender
        self.receiver = receiver
        self.date = datetime.datetime.now()
        self.state = 'pending'

    def delete_invite(self):
        self.sender = None
        self.receiver = None
        self.date = None
        self.state = None
