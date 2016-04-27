class Direction:

    directions = {
        1: "NORTH",
        2: "EAST",
        3: "SOUTH",
        4: "WEST"
    }

    def __init__(self):
        pass

    @staticmethod
    def validatedirection(direction):
        if direction in Direction.directions.values():
            return True
        else:
            return False

    @staticmethod
    def getdirection(directionindex):
        return Direction.directions[directionindex]

    @staticmethod
    def getdirectionindex(directionname):
        for index, direction in Direction.directions.items():
            if direction == directionname:
                return index
