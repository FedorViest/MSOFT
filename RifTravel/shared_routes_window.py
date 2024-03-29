from PyQt5 import QtCore, QtGui, QtWidgets

import utils
from GUI.main_menu import Ui_MainWindow

# class for displaying window containing all shared routes


class Ui_SharedRoutesWindow(object):

    # function for when "Back" button is clicked - returns to main menu

    def back(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as e:
            print(e)

    def setupUi(self, SharedRoutesWindow):
        SharedRoutesWindow.setObjectName("SharedRoutesWindow")
        SharedRoutesWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SharedRoutesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(230, 10, 311, 71))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 781, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())

        self.fill_route_info()

        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(320, 480, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backbtn.setFont(font)
        self.backbtn.setObjectName("backbtn")

        self.backbtn.clicked.connect(SharedRoutesWindow.close)
        self.backbtn.clicked.connect(self.back)

        SharedRoutesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SharedRoutesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SharedRoutesWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SharedRoutesWindow)
        self.statusbar.setObjectName("statusbar")
        SharedRoutesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SharedRoutesWindow)
        QtCore.QMetaObject.connectSlotsByName(SharedRoutesWindow)

    # function for filling textAreas with route details stored in utils.shared_routes. Function cycles through all
    # shared routes and creates textArea for each one of them. Each textArea contains route information along with
    # the name of route author, who shared the route. Route authors are stored in utils.shared_routes_authors list.

    def fill_route_info(self):
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

        for i in range(len(utils.shared_routes)):
            self.route_info = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
            self.route_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.route_info.setObjectName("route_info")
            self.verticalLayout.addWidget(self.route_info)
            string = "ROUTE: " + str(i + 1) + "\t\tAuthor: " + str(utils.route_authors[i].name) + \
                     "\nStart: " + utils.shared_routes[i].start + "\t\tActivities: " + str(utils.shared_routes[i].activities) + \
                     "\nEnd: " + utils.shared_routes[i].end + "\t\tStops: " + str(utils.shared_routes[i].stops) + \
                     "\nLength: " + str(utils.shared_routes[i].length) + "\t\tSeverity: " + str(utils.shared_routes[i].severity) + \
                     "\nWeather: " + "sunny" if utils.shared_routes[i].weather is None else "Sunny"
            self.route_info.setText(string)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


    def retranslateUi(self, SharedRoutesWindow):
        _translate = QtCore.QCoreApplication.translate
        SharedRoutesWindow.setWindowTitle(_translate("SharedRoutesWindow", "MainWindow"))
        self.textBrowser_2.setHtml(_translate("SharedRoutesWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">Shared Routes</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt; font-weight:600;\"><br /></p></body></html>"))
        self.backbtn.setText(_translate("SharedRoutesWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SharedRoutesWindow = QtWidgets.QMainWindow()
    ui = Ui_SharedRoutesWindow()
    ui.setupUi(SharedRoutesWindow)
    SharedRoutesWindow.show()
    sys.exit(app.exec_())
