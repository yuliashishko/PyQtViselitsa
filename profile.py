# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Profile(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(459, 322)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 30, 211, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formLayoutWidget.sizePolicy().hasHeightForWidth())
        self.formLayoutWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.name = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.username = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username)
        self.levelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelLabel.sizePolicy().hasHeightForWidth())
        self.levelLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.levelLabel.setFont(font)
        self.levelLabel.setObjectName("levelLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.levelLabel)
        self.level = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.level.sizePolicy().hasHeightForWidth())
        self.level.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.level.setFont(font)
        self.level.setObjectName("level")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.level)
        self.totalExpLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalExpLabel.sizePolicy().hasHeightForWidth())
        self.totalExpLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalExpLabel.setFont(font)
        self.totalExpLabel.setObjectName("totalExpLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.totalExpLabel)
        self.totalExp = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalExp.sizePolicy().hasHeightForWidth())
        self.totalExp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalExp.setFont(font)
        self.totalExp.setObjectName("totalExp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.totalExp)
        self.gamesLostLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamesLostLabel.sizePolicy().hasHeightForWidth())
        self.gamesLostLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamesLostLabel.setFont(font)
        self.gamesLostLabel.setObjectName("gamesLostLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gamesLostLabel)
        self.gamesLost = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamesLost.sizePolicy().hasHeightForWidth())
        self.gamesLost.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamesLost.setFont(font)
        self.gamesLost.setObjectName("gamesLost")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gamesLost)
        self.gamesWonLabel = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamesWonLabel.sizePolicy().hasHeightForWidth())
        self.gamesWonLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamesWonLabel.setFont(font)
        self.gamesWonLabel.setObjectName("gamesWonLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.gamesWonLabel)
        self.gamesWon = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamesWon.sizePolicy().hasHeightForWidth())
        self.gamesWon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamesWon.setFont(font)
        self.gamesWon.setObjectName("gamesWon")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.gamesWon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 30, 160, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.logoutButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout.addWidget(self.logoutButton)
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.createButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        self.levelProgress = QtWidgets.QProgressBar(Dialog)
        self.levelProgress.setGeometry(QtCore.QRect(60, 270, 371, 23))
        self.levelProgress.setProperty("value", 0)
        self.levelProgress.setObjectName("levelProgress")
        self.currentExp = QtWidgets.QLabel(Dialog)
        self.currentExp.setGeometry(QtCore.QRect(60, 240, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.currentExp.setFont(font)
        self.currentExp.setObjectName("currentExp")
        self.maxExp = QtWidgets.QLabel(Dialog)
        self.maxExp.setGeometry(QtCore.QRect(370, 240, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.maxExp.setFont(font)
        self.maxExp.setObjectName("maxExp")
        self.fromLabel = QtWidgets.QLabel(Dialog)
        self.fromLabel.setGeometry(QtCore.QRect(230, 240, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nameLabel.setText(_translate("Dialog", "Name"))
        self.name.setText(_translate("Dialog", "Guest"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.username.setText(_translate("Dialog", "not stated"))
        self.levelLabel.setText(_translate("Dialog", "Level"))
        self.level.setText(_translate("Dialog", "0"))
        self.totalExpLabel.setText(_translate("Dialog", "Total exp"))
        self.totalExp.setText(_translate("Dialog", "0"))
        self.gamesLostLabel.setText(_translate("Dialog", "Games lost"))
        self.gamesLost.setText(_translate("Dialog", "0"))
        self.gamesWonLabel.setText(_translate("Dialog", "Games won"))
        self.gamesWon.setText(_translate("Dialog", "0"))
        self.deleteButton.setText(_translate("Dialog", "Delete profile"))
        self.logoutButton.setText(_translate("Dialog", "Logout"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.createButton.setText(_translate("Dialog", "Create profile"))
        self.currentExp.setText(_translate("Dialog", "0"))
        self.maxExp.setText(_translate("Dialog", "10"))
        self.fromLabel.setText(_translate("Dialog", "????"))
