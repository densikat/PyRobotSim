from Commands import Command


class MoveCommand(Command.Command):

    def initializecommand(self, command):
        self.commandname = "MOVE"

    def __init__(self):
        pass

    def validateinstruction(self, robot, table):
        if table.currentrobot == robot:
            # If robot is facing north or south then get new vertical location
            if robot.direction == 1 or robot.direction == 3:
                newylocation = robot.newverticallocation()
                if 0 <= newylocation <= table.height:
                    return True
            else:
                newxlocation = robot.newhorizontallocation()
                if 0 <= newxlocation <= table.width:
                    return True

        return False

    def executeinstruction(self, robot, table):

        if robot.direction == 1:  # North
            self.__north(robot)
        elif robot.direction == 2:  # East
            self.__east(robot)
        elif robot.direction == 3:  # South
            self.__south(robot)
        elif robot.direction == 4:  # West
            self.__west(robot)

    @staticmethod
    def __north(robot):
        robot.height = robot.height + robot.movelength

    @staticmethod
    def __south(robot):
        robot.height = robot.height - robot.movelength

    @staticmethod
    def __east(robot):
        robot.width = robot.width + robot.movelength

    @staticmethod
    def __west(robot):
        robot.width = robot.width - robot.movelength









