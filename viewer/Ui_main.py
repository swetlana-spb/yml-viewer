# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tblOffers = QtWidgets.QTableView(self.centralwidget)
        self.tblOffers.setObjectName("tblOffers")
        self.gridLayout.addWidget(self.tblOffers, 0, 0, 1, 3)
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout.addWidget(self.btnRefresh, 1, 2, 1, 1)
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout.addWidget(self.btnConnect, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 22))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.menuConnection.addAction(self.actionSettings)
        self.menuConnection.addSeparator()
        self.menuConnection.addAction(self.actionExit)
        self.menubar.addAction(self.menuConnection.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.menuConnection.setTitle(_translate("MainWindow", "&Connection"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))

