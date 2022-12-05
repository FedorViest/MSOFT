import datetime

from PyQt5.uic.properties import QtCore, QtGui
from pyqt5_plugins.examplebutton import QtWidgets
from main import User, Route, SavedRoute, Stop, Accomodation, Activity, Weather, Rating

activities = ["bike", "run", "walk", "swim", "ski", "hike", "climb", "ride", "other"]
start_location_list = ["Select start location", "kokot", "pica", "u", "holica", "juraj", "vincur", "je", "kurac"]
end_location_list = ["Select end location", "kokot", "pica", "u", "holica", "juraj", "vincur", "je", "kurac"]
user = User("John John", "john@gmail.com", "123456", 20, 5, None)

route_1 = SavedRoute("London", "Paris", 20, 3, ["bike", "run", "walk"], ["campsite 1", "campsite 2"], None, None, datetime.datetime.now())
route_2 = SavedRoute("London", "Paris", 50, 8, ["ski", "swim", "walk"], ["hotel 1", "hotel 2"], None, None, datetime.datetime.now())
my_routes = [route_1, route_2]

def combobox_start(self):
    self.start_location_combo = QtWidgets.QComboBox(self.centralwidget)
    self.start_location_combo.setGeometry(QtCore.QRect(210, 290, 151, 22))
    self.start_location_combo.setCurrentText("Select start location")
    self.start_location_combo.setObjectName("start_location_combo")

    self.start_location_combo.addItems(start_location_list)


"""def activities_checkbox(self):

    activities = ["bike", "run", "walk", "swim", "ski", "hike", "climb", "ride", "other"]

    self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
    self.scrollArea.setGeometry(QtCore.QRect(30, 290, 140, 100))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
    self.scrollArea.setSizePolicy(sizePolicy)
    self.scrollArea.setMinimumSize(QtCore.QSize(0, 100))
    self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
    self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setObjectName("scrollArea")
    self.scrollAreaWidgetContents = QtWidgets.QWidget()
    self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 121, 186))
    self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
    self.verticalLayout.setObjectName("verticalLayout")

    for i in range(len(activities)):
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setText(activities[i])
        self.checkBox.setGeometry(QtCore.QRect(30, 280+(i*30), 151, 22))
        self.checkBox.setObjectName("activity_checkBox_{}".format(i))
        self.checkBox.stateChanged.connect(self.activities_checkbox)
        self.verticalLayout.addWidget(self.checkBox)

    self.scrollArea.setWidget(self.scrollAreaWidgetContents)"""
