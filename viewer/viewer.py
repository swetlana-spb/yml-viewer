import sys
from viewer.Ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui
from database import Database
from viewer.settings import Settings


class Viewer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db = None
        self.host = '127.0.0.1'
        self.port = 6379
        self.password = None
        self.setupUi(self)
        self.setWindowTitle('Data in redis database')
        self.statusbar.showMessage('Not connected')
        self.tblOffers.setMinimumSize(400, 300)
        self.settings = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
        self.load_settings()
        self.actionExit.triggered.connect(sys.exit)
        self.btnConnect.clicked.connect(self.connect)
        self.btnRefresh.clicked.connect(self.refresh)
        self.actionSettings.triggered.connect(self.settings_dialog)

    def load_settings(self):
        self.host = self.settings.value('host')
        self.port = self.settings.value('port')
        self.password = self.settings.value('password')

    def fill_table(self, data):
        model = OffersModel(self.tblOffers, data)
        self.tblOffers.setModel(model)

    def connect(self):
        try:
            self.db = Database(self.host, self.port, self.password)
            self.refresh()
        except:
            QMessageBox.critical(self, 'Error', 'Connection to {0}:{1} failed.'.format(self.host, self.port))

    def settings_dialog(self):
        settings = Settings()
        settings.exec_()
        self.load_settings()

    def refresh(self):
        data = self.db.download_data()
        if data:
            self.fill_table(data)
            self.statusbar.showMessage('Data from {0}:{1} received'.format(self.host, self.port))


class OffersModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, data_table):
        QtCore.QAbstractTableModel.__init__(self)
        self.gui = parent
        self.colLabels = ['Category', 'Name', 'Price']
        self.data_table = data_table

    def rowCount(self, parent):
        return len(self.data_table)

    def columnCount(self, parent):
        return len(self.colLabels)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.data_table[row][col].decode('utf-8')
            return QtCore.QVariant(value)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.colLabels[section])
        return QtCore.QVariant()
