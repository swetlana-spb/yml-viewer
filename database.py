import redis


class Database(object):
    def __init__(self, host=None, port=None, password=None):
        self.db = redis.Redis(host=host if host else '127.0.0.1',
                                      port=port if port else '6379',
                                      password=password if password else None)

    def upload_data(self, data):
        for key, value in data.items():
            '''This may be a problem for a large amount of data, but must be ok for the example.
            Using pipeline() will be more suitable for a large amount of data.'''
            self.db.set(key, value)

    def download_data(self):
        data_list = []
        for key in self.db.keys():
            if key.startswith(b'yml-offer_'):
                value_list = self.db.mget(key)
                for value in value_list:
                    if isinstance(value, bytes):
                        row = value.split(b':')
                        data_list.append(row)
        return data_list
