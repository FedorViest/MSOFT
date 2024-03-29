from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.main_menu import Ui_MainWindow

# class for the route confirmation window


class Ui_RouteRecap(object):

    # Method for opening the main menu window when route to be created is confirmed
    # called when the "Confirm" button is clicked

    def confirm_route(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, RouteRecap):
        RouteRecap.setObjectName("RouteRecap")
        RouteRecap.resize(649, 150)
        self.Backbtn = QtWidgets.QPushButton(RouteRecap)
        self.Backbtn.setGeometry(QtCore.QRect(40, 60, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Backbtn.setFont(font)
        self.Backbtn.setObjectName("Backbtn")
        self.Backbtn.clicked.connect(RouteRecap.close)

        self.Confirmbtn = QtWidgets.QPushButton(RouteRecap)
        self.Confirmbtn.setGeometry(QtCore.QRect(370, 60, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Confirmbtn.setFont(font)
        self.Confirmbtn.setObjectName("Confirmbtn")
        self.Confirmbtn.clicked.connect(self.confirm_route)
        self.Confirmbtn.clicked.connect(RouteRecap.close)

        self.textBrowser_2 = QtWidgets.QTextBrowser(RouteRecap)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 10, 250, 41))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(RouteRecap)
        QtCore.QMetaObject.connectSlotsByName(RouteRecap)

    def retranslateUi(self, RouteRecap):
        _translate = QtCore.QCoreApplication.translate
        RouteRecap.setWindowTitle(_translate("RouteRecap", "Dialog"))
        self.Backbtn.setText(_translate("RouteRecap", "Back"))
        self.Confirmbtn.setText(_translate("RouteRecap", "Confirm"))
        self.textBrowser_2.setHtml(_translate("RouteRecap",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Confirm route</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RouteRecap = QtWidgets.QDialog()
    ui = Ui_RouteRecap()
    ui.setupUi(RouteRecap)
    RouteRecap.show()
    sys.exit(app.exec_())
