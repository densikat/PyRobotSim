from Commands import Command


class Robot:

    __width = None
    _height = None
    _direction = None

    def __init__(self):
        self.movelength = 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height  = height

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def NewHorizontalLocation(self):
        if self.direction == 2:
            return self.width + self.movelength
        else:
            return self.width - self.movelength

    def NewVerticalLocation(self):
        if self.direction == 1:
            return self.height + self.movelength
        else:
            return self.height - self.movelength


    def executeinstruction(self, command, table):
        if command.validateinstruction(self, table):
            command.executeinstruction(self, table)

