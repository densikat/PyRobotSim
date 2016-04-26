import Commands
from Commands import Command
import Direction


class ReportCommand(Commands.Command.Command):
    def __init__(self):
        pass

    def executeinstruction(self, robot, table):
        print("{0}, {1}, {2}".format(robot.width, robot.height, Direction.Direction.getdirection(robot.direction)))

    def validateinstruction(self, robot, table):
        if table.currentrobot == robot:
            return True
        else:
            return False

    def initializecommand(self, command):
        self.commandname = "REPORT"