import redis


class DatabaseWorker(object):
    def __init__(self, host=None, port=None, password=None):
        self.connection = redis.Redis(host=host if host else '127.0.0.1',
                                      port=port if port else '6379',
                                      password=password if password else None)

    def upload_data(self, data):
        for key, value in data.items():
            self.connection.set(key, value)

    def download_data(self):
        data_list = []
        for key in self.connection.keys():
            value_list = self.connection.mget(key)
            for value in value_list:
                value = value.split(b':')
            data_list.append(value)
        return data_list
