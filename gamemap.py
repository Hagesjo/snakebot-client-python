class GameMap(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)
        self.methods = entries

    def methods_available(self):
        return self.methods.keys()
