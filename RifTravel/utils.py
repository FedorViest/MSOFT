import datetime
# from main import User, Route, SavedRoute, Stop, Accomodation, Activity, Weather, Rating
#from Route_info.route_info import Route, SavedRoute
import Route_info
import User_info
from User_info import user_info

activities = ["bike", "run", "swim", "barbeque", "hike", "rock-climb", "rollerskates", "bunjee-jumping"]
start_location_list = ["Select start location", "Belusa", "Beckov", "Tomasov", "Jelka", "Cerveny Klastor", "Szczawnica",
                       "Podbanské (Kokavský most)", "Pribilina"]
end_location_list = ["Select end location", "Belusa", "Beckov", "Tomasov", "Jelka", "Cerveny Klastor", "Szczawnica",
                       "Podbanské (Kokavský most)", "Pribilina"]
route = Route_info.route_info.Route("start", "end", 10, 5, None, None, None)

route_1 = Route_info.route_info.SavedRoute("Belusa", "Beckov", 20, 3, ["bike", "bunjee-jumping", "walk"], ["campsite 1", "campsite 2"],
                     None, datetime.datetime.now())
route_2 = Route_info.route_info.SavedRoute("Podbanske (Kokavsky most)", "Pribilina", 50, 8, ["rollerskates", "swim", "rock-climb"],
                     ["hotel 1", "hotel 2"], None, datetime.datetime.now())
my_routes = [route_2]


shared_route_1 = Route_info.route_info.Route("Belusa", "Beckov", 20, 3, ["bike", "bunjee-jumping", "walk"], ["campsite 1", "campsite 2"],
                     None)
shared_route_2 = Route_info.route_info.Route("Podbanske (Kokavsky most)", "Pribilina", 50, 8, ["rollerskates", "swim", "rock-climb"],
                     ["hotel 1", "hotel 2"], None)

user = User_info.user_info.User("Richard", "richard.17@pokec.sk", "password", 33)

curr_user = User_info.user_info.User("Jozef Mrkva", "jozef.mrkva@gmail.com", "password123", 25)

route_author = User_info.user_info.RouteAuthor("Richard", "richard.17@pokec.sk", "password", 33, 1)

route_authors = [route_author]

shared_routes = [shared_route_1]
