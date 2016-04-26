import Commands
from Commands import Command

class RightCommand(Commands.Command.Command):
    def __init__(self):
        pass

    def executeinstruction(self, robot, table):
        if robot.direction == 4:
            newdirection = 1
        else:
            newdirection = robot.direction + 1

        robot.direction = newdirection


    def validateinstruction(self, robot, table):
        if table.currentrobot == robot:
            return True
        else:
            return False

    def initializecommand(self, command):
        self.commandname = "RIGHT"