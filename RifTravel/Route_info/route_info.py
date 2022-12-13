import User_info.user_info
from GUI.Route_confirmation import Ui_RouteRecap
from GUI.main_menu import Ui_MainWindow
from GUI.share_unable_window import Ui_UnableShareWindow
from GUI.unable_window import Ui_UnableWindow

from PyQt5 import QtWidgets
from Functionalities.functionalities import Weather
from Stops.stops import Booking
import datetime
import random
import utils


class Activity(Booking):
    def __init__(self, min_age: int, type: str, price: int):
        self.min_age = min_age
        self.type = type
        self.price = price

    def book(self):
        pass

    def add_activities(self):
        return Route

    def remove_activity(self):
        pass


class Route:
    def __init__(self, start: str, end: str, length: int, severity: int, activities: list, stops: list, weather: Weather = None):
        self.start = start
        self.end = end
        self.length = length
        self.severity = severity
        self.activities = activities
        self.stops = stops
        self.weather = weather

    def save_route(self, route):
        saved_route = SavedRoute(route.start, route.end, route.length, route.severity, route.activities, route.stops,
                          route.weather, datetime.date.today())
        import utils
        utils.my_routes.append(saved_route)

        return saved_route

    def share_route(self, saved_route):
        for shared_route in utils.shared_routes:
            if shared_route.start == saved_route.start and shared_route.end == saved_route.end and \
                    shared_route.activities == saved_route.activities:
                print("Unable to share selected route")
                try:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_UnableShareWindow()
                    self.ui.setupUi(self.window)
                    self.window.show()
                except Exception as e:
                    print(e)
                return None
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)
        route_author = User_info.user_info.RouteAuthor(utils.curr_user.name, utils.curr_user.email,
                                                       utils.curr_user.password, utils.curr_user.age, 1)
        utils.route_authors.append(route_author)
        utils.shared_routes.append(saved_route)
        return saved_route

    def create_route(self, route_details):

        activities = route_details[0]
        severity = int(route_details[1][0])
        travelling_as = route_details[2][0]
        sleeping = [route_details[2][1]]
        start_location = route_details[3][0]
        end_location = route_details[3][1]
        date = route_details[4][0]

        if start_location == end_location or len(activities) >= 5:
            print("Unable to create route")
            try:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_UnableWindow()
                self.ui.setupUi(self.window)
                self.window.show()
            except Exception as e:
                print(e)

        else:
            print("Route created")
            try:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_RouteRecap()
                self.ui.setupUi(self.window)
                self.window.show()
            except Exception as e:
                print(e)
            route = Route(start_location, end_location, random.randrange(10, 100), severity, activities, list(sleeping), None)
            saved_route = route.save_route(route)

            return saved_route

        return None

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
                 weather: Weather, date: datetime):
        super().__init__(start, end, length, severity, activities, stops, weather)
        self.date = date