# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(460, 328)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 250, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab1)
        self.pushButton.setGeometry(QtCore.QRect(350, 250, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab1)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 250, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.tab1)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 211, 20))
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(parent=self.tab1)
        self.line.setGeometry(QtCore.QRect(0, 60, 461, 31))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(parent=self.tab1)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(parent=self.tab1)
        self.line_2.setGeometry(QtCore.QRect(170, 80, 31, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.tab1)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 40, 171, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        TabWidget.addTab(self.tab1, "")
        self.actionnewPassword = QtGui.QAction(parent=TabWidget)
        self.actionnewPassword.setObjectName("actionnewPassword")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Passwordmanager"))
        self.label.setText(_translate("TabWidget", "Willkommen, Max!"))
        self.pushButton_3.setText(_translate("TabWidget", "New Password"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Home"))
        self.pushButton.setText(_translate("TabWidget", "Beenden"))
        self.pushButton_2.setText(_translate("TabWidget", "Security-Check"))
        self.checkBox.setText(_translate("TabWidget", "mit Standard-Browser nutzen"))
        self.label_2.setText(_translate("TabWidget", "Acccount:"))
        self.checkBox_2.setText(_translate("TabWidget", "beim Start öffnen"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Einstellungen"))
        self.actionnewPassword.setText(_translate("TabWidget", "newPassword"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec())
