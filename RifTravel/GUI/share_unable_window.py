from PyQt5 import QtCore, QtGui, QtWidgets

from main_menu import Ui_MainWindow

# class for creating window when selected route cannot be shared


class Ui_UnableShareWindow(object):

    # Method to open main menu window called when "OK" button is clicked

    def ok_pressed(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, UnableShareWindow):
        UnableShareWindow.setObjectName("UnableShareWindow")
        UnableShareWindow.resize(553, 191)
        self.textBrowser = QtWidgets.QTextBrowser(UnableShareWindow)
        self.textBrowser.setGeometry(QtCore.QRect(70, 10, 450, 91))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.ok_button = QtWidgets.QPushButton(UnableShareWindow)
        self.ok_button.setGeometry(QtCore.QRect(220, 130, 121, 41))
        self.ok_button.setObjectName("ok_button")

        self.ok_button.clicked.connect(self.ok_pressed)
        self.ok_button.clicked.connect(UnableShareWindow.close)

        self.retranslateUi(UnableShareWindow)
        QtCore.QMetaObject.connectSlotsByName(UnableShareWindow)

    def retranslateUi(self, UnableShareWindow):
        _translate = QtCore.QCoreApplication.translate
        UnableShareWindow.setWindowTitle(_translate("UnableShareWindow", "Dialog"))
        self.textBrowser.setHtml(_translate("UnableShareWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Unable to share route because it was already shared.</span></p></body></html>"))
        self.ok_button.setText(_translate("UnableShareWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnableShareWindow = QtWidgets.QDialog()
    ui = Ui_UnableShareWindow()
    ui.setupUi(UnableShareWindow)
    UnableShareWindow.show()
    sys.exit(app.exec_())
