import Robot
import Table
from Commands import CommandFactory


def processcommand(command):
    command = CommandFactory.CommandFactory.getclass(command)
    if command is not None:
        if command.commandname is not None:
            robot.executeinstruction(command, table)


def runinteractive():
    while True:
        cmdinput = input("")
        processcommand(cmdinput.upper())

if __name__ == '__main__':
    table = Table.Table(4, 4)
    robot = Robot.Robot()
    runinteractive()


