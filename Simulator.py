from Commands import CommandFactory,Command, MoveCommand
import Robot, Table


def processcommand(command):
    command = CommandFactory.CommandFactory.getclass(command)
    if (command is not None):
        robot.executeinstruction(command, table)

if __name__ == '__main__':
    table = Table.Table(4, 4)
    robot = Robot.Robot()

    processcommand("PLACE 1,1,EAST")
    processcommand("MOVE")
    processcommand("REPORT")
    processcommand("LEFT")
    processcommand("MOVE")
    processcommand("REPORT")

