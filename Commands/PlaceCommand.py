from Commands import Command
import Direction
import re


class PlaceCommand(Command.Command):
    def __init__(self):
        self.width = None
        self.height = None
        self.direction = None
        self.commandname = None

    def executeinstruction(self, robot, table):
        robot.width = self.width
        robot.height = self.height
        robot.direction = self.direction
        table.currentrobot = robot

    def initializecommand(self, command):

        validcommand = False

        split = command.split(" ")
        args = split[1]

        pattern = re.compile("-?\d{1},-?\d{1},\w{4,5}")

        if pattern.match(args):
            argsplit = args.split(',')
            # Make sure we have three arguments
            if len(argsplit) == 3:
                if Direction.Direction.validatedirection(argsplit[2]):
                    self.width = int(argsplit[0])
                    self.height = int(argsplit[1])
                    self.direction = Direction.Direction.getdirectionindex(argsplit[2])
                    self.commandname = "PLACE"
                    validcommand = True

        return validcommand

    def validateinstruction(self, robot, table):
        returnval = False

        if self.commandname == "PLACE" and table.currentrobot is None:
            if 0 <= int(self.width) <= table.width:
                if 0 <= int(self.height) <= table.height:
                    returnval = True

        return returnval


