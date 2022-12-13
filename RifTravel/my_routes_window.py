# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MyRoutesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

import utils


class Ui_MyRoutesWindow(QMainWindow):

    """def openMain(self):
        try:
            from main_menu import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)"""

    def share_route(self):
        sender = self.sender()
        index = int(sender.objectName().split("_")[1])
        utils.route.share_route(utils.my_routes[index])

    def back(self):
        try:
            from GUI.main_menu import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    def setupUi(self, MyRoutesWindow):
        MyRoutesWindow.setObjectName("MyRoutesWindow")
        MyRoutesWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MyRoutesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(280, 10, 221, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.fill_route_details(MyRoutesWindow)

        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(320, 480, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backbtn.setFont(font)
        self.backbtn.setObjectName("backbtn")

        self.backbtn.clicked.connect(self.back)
        self.backbtn.clicked.connect(MyRoutesWindow.close)


        MyRoutesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyRoutesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MyRoutesWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyRoutesWindow)
        self.statusbar.setObjectName("statusbar")
        MyRoutesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyRoutesWindow)
        QtCore.QMetaObject.connectSlotsByName(MyRoutesWindow)

    def fill_route_details(self, MyRoutesWindow):

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 781, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 758, 391))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in range(len(utils.my_routes)):
            self.route_info = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
            self.route_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.route_info.setObjectName("route_info")
            self.verticalLayout.addWidget(self.route_info)
            string = "ROUTE: " + str(i + 1) + "\nStart: " + utils.my_routes[i].start + "\t\tActivities: " + str(utils.my_routes[i].activities) + \
            "\nEnd: " + utils.my_routes[i].end + "\t\tStops: " + str(utils.my_routes[i].stops) + \
            "\nLength: " + str(utils.my_routes[i].length) + "\t\tSeverity: " + str(utils.my_routes[i].severity) + \
                "\nDate created: " + str(utils.my_routes[i].date) + "\t\tWeather: " + \
                     "sunny" if utils.my_routes[i].weather is None else "Sunny"
            self.route_info.setText(string)
            self.sharebtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.delbtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.sharebtn.setFont(font)
            self.delbtn.setFont(font)
            self.sharebtn.setObjectName("sharebtn_{i}".format(i=i))
            self.delbtn.setObjectName("delbtn{i}".format(i=i))
            self.sharebtn.setText("Share route {i}".format(i=i+1))
            self.delbtn.setText("Delete route {i}".format(i=i+1))
            self.verticalLayout.addWidget(self.sharebtn)
            self.verticalLayout.addWidget(self.delbtn)

            self.sharebtn.clicked.connect(MyRoutesWindow.close)

            self.sharebtn.clicked.connect(self.share_route)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def retranslateUi(self, MyRoutesWindow):
        _translate = QtCore.QCoreApplication.translate
        MyRoutesWindow.setWindowTitle(_translate("MyRoutesWindow", "MainWindow"))
        self.textBrowser_2.setHtml(_translate("MyRoutesWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">My routes</span></p></body></html>"))
        self.backbtn.setText(_translate("MyRoutesWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyRoutesWindow = QtWidgets.QMainWindow()
    ui = Ui_MyRoutesWindow()
    ui.setupUi(MyRoutesWindow)
    MyRoutesWindow.show()
    sys.exit(app.exec_())
