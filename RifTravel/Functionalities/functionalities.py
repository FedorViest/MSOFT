from datetime import datetime


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


class Invite:
    def __init__(self, date: datetime, state: str, sender: str, receiver: str):
        self.date = date
        self.state = state
        self.sender = sender
        self.receiver = receiver

    def accept(self):
        pass

    def reject(self):
        pass

    def create_invite(self, sender: str, receiver: str):
        pass

    def delete_invite(self):
        pass