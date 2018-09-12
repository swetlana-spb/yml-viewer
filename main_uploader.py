import argparse
import getpass
from parser import XmlParser
from database import Database


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)


def get_args():
    parser = argparse.ArgumentParser(description='Uploads data from .xml into redis database.')
    parser.add_argument('-f', '--fileName', help='path to a file', required=True)
    parser.add_argument('-H', '--host',
                        help='ip-address for the database',
                        required=False)
    parser.add_argument('-p', '--port',
                        help='port for the database',
                        required=False)
    parser.add_argument('-P', '--password',
                        action=Password,
                        nargs='?',
                        help='password for the database',
                        required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    db = Database(args.host, args.port, args.password)

    parser = XmlParser(args.fileName)
    data = parser.parse()
    if data:
        try:
            db.upload_data(data)
            print('Data uploaded. Bye! :)')
        except:
            print('Something went wrong :(')
    else:
        print('There is no data to upload :(')
