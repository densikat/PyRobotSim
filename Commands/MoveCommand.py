import abc
import Commands
from Commands import Command
import Robot, Table


class MoveCommand(Commands.Command.Command):

    def initializecommand(self, command):
        self.commandname = "MOVE"

    def __init__(self):
        self.commandname = "MOVE"

    def validateinstruction(self, robot, table):
        if table.currentrobot == robot:
            if robot.direction == 1 or robot.direction == 3:
                newylocation = robot.NewVerticalLocation()
                if 0 <= newylocation <= table.height:
                    return True
            else:
                newxlocation = robot.NewHorizontalLocation()
                if 0 <= newxlocation <= table.width:
                    return True

        return False

    def executeinstruction(self, robot, table):

        if robot.direction == 1:
            self.__north(robot)
        elif robot.direction == 2:
            self.__east(robot)
        elif robot.direction == 3:
            self.__south(robot)
        elif robot.direction == 4:
            self.__west(robot)

    def __north(self, robot):
        robot.height = robot.height + robot.movelength

    def __south(self, robot):
        robot.height = robot.height - robot.movelength

    def __east(self, robot):
        robot.width = robot.width + robot.movelength

    def __west(self, robot):
        robot.width = robot.width - robot.movelength









