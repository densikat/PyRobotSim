class Table:
    _currentrobot = None

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def currentrobot(self):
        return self._currentrobot

    @currentrobot.setter
    def currentrobot(self, robot):
        self._currentrobot = robot


