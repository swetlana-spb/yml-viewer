# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        Viewer.setObjectName("Viewer")
        Viewer.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Viewer)
        self.gridLayout.setObjectName("gridLayout")
        self.tblOffers = QtWidgets.QTableView(Viewer)
        self.tblOffers.setObjectName("tblOffers")
        self.gridLayout.addWidget(self.tblOffers, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Viewer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Viewer)
        self.buttonBox.accepted.connect(Viewer.accept)
        self.buttonBox.rejected.connect(Viewer.reject)
        QtCore.QMetaObject.connectSlotsByName(Viewer)

    def retranslateUi(self, Viewer):
        _translate = QtCore.QCoreApplication.translate
        Viewer.setWindowTitle(_translate("Viewer", "Dialog"))

