from abc import ABC, abstractmethod
from Functionalities.functionalities import Weather, Location, Rating, Invite

class Booking(ABC):

    @abstractmethod
    def book(self):
        pass

class Stop:
    def __int__(self, rating: Rating, type: str, price: int):
        self.rating = rating
        self.type = type
        self.price = price

    def add_stops(self):
        return None

    def remove_stop(self):
        pass


class Accomodation(Stop, Booking):
    def __init__(self, rating: Rating, type: str, price: int, accomodation_type: str):
        super().__init__(rating, type, price)
        self.accomodation_type = accomodation_type

    def book(self):
        pass