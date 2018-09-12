from viewer.ui_viewer import Ui_Viewer
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore


class Viewer(QDialog, Ui_Viewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Data in redis database')

    def fill_table(self, data):
        model = OffersModel(self.tblOffers, data)
        self.tblOffers.setModel(model)


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



