class GameMap(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)
        self.data = entries

    def data_available(self):
        return self.data.keys()
