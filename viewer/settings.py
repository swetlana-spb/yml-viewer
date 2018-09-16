from PyQt5.QtWidgets import QDialog
from viewer.Ui_Settings import Ui_Settings

class Settings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Settings')
