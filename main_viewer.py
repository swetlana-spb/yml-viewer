import sys
from PyQt5 import QtWidgets
from viewer.viewer import Viewer


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    viewer = Viewer()
    viewer.show()
    sys.exit(app.exec_())
