from PyQt5 import QtCore, QtGui, QtWidgets

from main_menu import Ui_MainWindow

# class for displaying error while creating route, saying that it cannot be created with specified parameters


class Ui_UnableWindow(object):

    # Method to open main menu window called when "OK" button is clicked

    def ok_pressed(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, UnableWindow):
        UnableWindow.setObjectName("UnableWindow")
        UnableWindow.resize(553, 191)
        self.textBrowser = QtWidgets.QTextBrowser(UnableWindow)
        self.textBrowser.setGeometry(QtCore.QRect(70, 10, 400, 91))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.ok_button = QtWidgets.QPushButton(UnableWindow)
        self.ok_button.setGeometry(QtCore.QRect(220, 130, 121, 41))
        self.ok_button.setObjectName("ok_button")

        self.ok_button.clicked.connect(self.ok_pressed)
        self.ok_button.clicked.connect(UnableWindow.close)

        self.retranslateUi(UnableWindow)
        QtCore.QMetaObject.connectSlotsByName(UnableWindow)

    def retranslateUi(self, UnableWindow):
        _translate = QtCore.QCoreApplication.translate
        UnableWindow.setWindowTitle(_translate("UnableWindow", "Dialog"))
        self.textBrowser.setHtml(_translate("UnableWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Unable to create route with specified parameters.</span></p></body></html>"))
        self.ok_button.setText(_translate("UnableWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnableWindow = QtWidgets.QDialog()
    ui = Ui_UnableWindow()
    ui.setupUi(UnableWindow)
    UnableWindow.show()
    sys.exit(app.exec_())
