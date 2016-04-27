import Robot
import Table
from Commands import CommandFactory


def processcommand(command, robot):
    command = CommandFactory.CommandFactory.getclass(command)
    if command is not None:
        if command.commandname is not None:
            robot.executeinstruction(command, table)


def runinteractive(robot):
    while True:
        cmdinput = input("")
        processcommand(cmdinput.upper(), robot)

if __name__ == '__main__':
    table = Table.Table(4, 4)
    __robot = Robot.Robot()
    runinteractive(__robot)
