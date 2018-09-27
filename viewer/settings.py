from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings, QVariant
from viewer.Ui_Settings import Ui_Settings


class Settings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Settings')
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.load_settings()

    def load_settings(self):
        self.edtHost.setText(self.settings.value('host'))
        self.edtPort.setText(self.settings.value('port'))
        self.edtPassword.setText(self.settings.value('password'))

    def done(self, event):
        self.settings.setValue('host', QVariant(self.edtHost.text()))
        self.settings.setValue('port', QVariant(self.edtPort.text()))
        """Yes, store password like that is a very bad idea.
        So I will do some hashing stuff with is a bit later"""
        self.settings.setValue('password', QVariant(self.edtPassword.text()))
        self.settings.sync()
        super().done(event)
