# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lost.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lost(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Lost")
        Dialog.resize(588, 405)
        self.textLabel = QtWidgets.QLabel(Dialog)
        self.textLabel.setGeometry(QtCore.QRect(110, 40, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textLabel.setFont(font)
        self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel.setObjectName("textLabel")
        self.gifLabel = QtWidgets.QLabel(Dialog)
        self.gifLabel.setGeometry(QtCore.QRect(50, 100, 306, 258))
        self.gifLabel.setObjectName("gifLabel")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(370, 100, 141, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.playersLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.playersLabel.setObjectName("playersLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.playersLabel)
        self.players = QtWidgets.QLabel(self.formLayoutWidget)
        self.players.setObjectName("players")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.players)
        self.wonLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.wonLabel.setObjectName("wonLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wonLabel)
        self.persent = QtWidgets.QLabel(self.formLayoutWidget)
        self.persent.setObjectName("persent")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.persent)
        self.percentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.percentLabel.setObjectName("percentLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.percentLabel)
        self.won = QtWidgets.QLabel(self.formLayoutWidget)
        self.won.setObjectName("won")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.won)
        self.menuButton = QtWidgets.QPushButton(Dialog)
        self.menuButton.setGeometry(QtCore.QRect(370, 210, 141, 41))
        self.menuButton.setObjectName("menuButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textLabel.setText(_translate("Dialog", "You lost :("))
        self.gifLabel.setText(_translate("Dialog", "gif"))
        self.playersLabel.setText(_translate("Dialog", "Всего игроков"))
        self.players.setText(_translate("Dialog", "0"))
        self.wonLabel.setText(_translate("Dialog", "Выигрышей"))
        self.persent.setText(_translate("Dialog", "0"))
        self.percentLabel.setText(_translate("Dialog", "Процент побед"))
        self.won.setText(_translate("Dialog", "0"))
        self.menuButton.setText(_translate("Dialog", "Menu"))
