import sys
from Commands import Command


class ExitCommand(Command.Command):
    def __init__(self):
        pass

    def executeinstruction(self, robot, table):
        sys.exit(0)

    def validateinstruction(self, robot, table):
        return True

    def initializecommand(self, command):
        self.commandname = "EXIT"
