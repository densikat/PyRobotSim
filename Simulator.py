import Robot
import Table
from Commands import CommandFactory


def processcommand(command, robot, table):
    command = CommandFactory.CommandFactory.getclass(command)
    if command is not None:
        if command.commandname is not None:
            robot.executeinstruction(command, table)


def runinteractive(robot, table):
    while True:
        cmdinput = input("")
        processcommand(cmdinput.upper(), robot, table)

if __name__ == '__main__':
    __table = Table.Table(4, 4)
    __robot = Robot.Robot()
    runinteractive(__robot, __table)
