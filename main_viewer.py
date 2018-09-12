import sys
import argparse
import getpass
from PyQt5 import QtWidgets, QtGui
from viewer.viewer import Viewer
from database import DatabaseWorker


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)


def create_args_parser():
    parser = argparse.ArgumentParser(description='Shows data from redis database.')
    parser.add_argument('-H', '--host',
                        help='ip-address of the database',
                        required=False)
    parser.add_argument('-p', '--port',
                        help='port of the database',
                        required=False)
    parser.add_argument('-P', '--password',
                        action=Password,
                        nargs='?',
                        help='password to the database',
                        required=False)
    return parser


if __name__ == "__main__":
    args_parser = create_args_parser()
    args = args_parser.parse_args()
    app = QtWidgets.QApplication(sys.argv)
    viewer = Viewer()
    db_worker = DatabaseWorker(args.host, args.port, args.password)
    data = db_worker.download_data()
    viewer.fill_table(data)
    viewer.show()
    sys.exit(app.exec_())

