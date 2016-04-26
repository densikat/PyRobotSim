import Commands
from Commands import Command

class LeftCommand(Commands.Command.Command):
    def __init__(self):
        pass

    def executeinstruction(self, robot, table):
        if robot.direction == 1:
            newdirection = 4
        else:
            newdirection = robot.direction - 1

        robot.direction = newdirection

    def validateinstruction(self, robot, table):
        if table.currentrobot == robot:
            return True
        else:
            return False

    def initializecommand(self, command):
        self.commandname = "LEFT"