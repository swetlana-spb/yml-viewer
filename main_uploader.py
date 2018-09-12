import argparse
import getpass
from parser import XmlParser
from database import DatabaseWorker


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)


def create_args_parser():
    parser = argparse.ArgumentParser(description='Uploading data from .xml into redis database.')
    parser.add_argument('-f', '--fileName', help='path to a file', required=True)
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


if __name__ == '__main__':
    args_parser = create_args_parser()
    args = args_parser.parse_args()
    db_worker = DatabaseWorker(args.host, args.port, args.password)

    parser = XmlParser(args.fileName)
    data = parser.parse()
    if data:
        try:
            db_worker.upload_data(data)
            print('Data uploaded. Bye!')
        except:
            print('Something go wrong :(')
    else:
        print('There is no data to upload :(')
