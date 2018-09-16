# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(184, 136)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.lblHost = QtWidgets.QLabel(Settings)
        self.lblHost.setObjectName("lblHost")
        self.gridLayout.addWidget(self.lblHost, 0, 0, 1, 1)
        self.edtHost = QtWidgets.QLineEdit(Settings)
        self.edtHost.setObjectName("edtHost")
        self.gridLayout.addWidget(self.edtHost, 0, 1, 1, 1)
        self.lblPort = QtWidgets.QLabel(Settings)
        self.lblPort.setObjectName("lblPort")
        self.gridLayout.addWidget(self.lblPort, 1, 0, 1, 1)
        self.edtPort = QtWidgets.QLineEdit(Settings)
        self.edtPort.setMaxLength(6)
        self.edtPort.setObjectName("edtPort")
        self.gridLayout.addWidget(self.edtPort, 1, 1, 1, 1)
        self.lblPassword = QtWidgets.QLabel(Settings)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 2, 0, 1, 1)
        self.edtPassword = QtWidgets.QLineEdit(Settings)
        self.edtPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.edtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtPassword.setObjectName("edtPassword")
        self.gridLayout.addWidget(self.edtPassword, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept)
        self.buttonBox.rejected.connect(Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.lblHost.setText(_translate("Settings", "Host"))
        self.edtHost.setInputMask(_translate("Settings", "000.000.000.000"))
        self.edtHost.setText(_translate("Settings", "127.0.0.1"))
        self.lblPort.setText(_translate("Settings", "Port"))
        self.edtPort.setInputMask(_translate("Settings", "000000"))
        self.edtPort.setText(_translate("Settings", "6379"))
        self.lblPassword.setText(_translate("Settings", "Password"))

