from PyQt5 import QtCore, QtGui, QtWidgets

# class for the main menu window


class Ui_MainWindow(object):

    # Method to open the window for creating a new route surrounded by a try/except block
    # called when the "Create Route" button is clicked

    def create_route_open(self):
        try:
            from create_route_window import Ui_CreateRouteWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_CreateRouteWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    # Method to open the window for displaying all of current users' saved routes surrounded by a try/except block
    # called when the "My Routes" button is clicked

    def open_my_routes(self):
        try:
            from my_routes_window import Ui_MyRoutesWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MyRoutesWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    # Method to open the window for displaying all shared routes in application surrounded by a try/except block
    # called when the "Shared Routes" button is clicked

    def open_shared_routes(self):
        try:
            from shared_routes_window import Ui_SharedRoutesWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SharedRoutesWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sharedroutesbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sharedroutesbtn.setGeometry(QtCore.QRect(220, 290, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sharedroutesbtn.setFont(font)
        self.sharedroutesbtn.setObjectName("sharedroutesbtn")

        self.sharedroutesbtn.clicked.connect(self.open_shared_routes)
        self.sharedroutesbtn.clicked.connect(MainWindow.close)

        self.myRoutesbtn = QtWidgets.QPushButton(self.centralwidget)
        self.myRoutesbtn.setGeometry(QtCore.QRect(220, 190, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.myRoutesbtn.setFont(font)
        self.myRoutesbtn.setObjectName("myRoutesbtn")

        self.myRoutesbtn.clicked.connect(self.open_my_routes)
        self.myRoutesbtn.clicked.connect(MainWindow.close)

        self.createRoutebtn = QtWidgets.QPushButton(self.centralwidget)
        self.createRoutebtn.setGeometry(QtCore.QRect(220, 90, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.createRoutebtn.setFont(font)
        self.createRoutebtn.setObjectName("createRoutebtn")

        self.createRoutebtn.clicked.connect(self.create_route_open)
        self.createRoutebtn.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sharedroutesbtn.setText(_translate("MainWindow", "Shared Routes"))
        self.myRoutesbtn.setText(_translate("MainWindow", "My Routes"))
        self.createRoutebtn.setText(_translate("MainWindow", "Create Route"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
