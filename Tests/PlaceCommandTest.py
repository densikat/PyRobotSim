import unittest
import Commands.PlaceCommand
import Robot, Table

class PlaceCommandTest(unittest.TestCase):
    def test_validplacestring(self):
        command = Commands.PlaceCommand.PlaceCommand()
        self.assertTrue(command.initializecommand("PLACE 0,0,NORTH"))

    def test_invalidplacestring(self):
        command = Commands.PlaceCommand.PlaceCommand()
        self.assertFalse(command.initializecommand("PLACE 0,0,NSORTH"))

    def test_invalidcoorddatatype(self):
        command = Commands.PlaceCommand.PlaceCommand()
        self.assertFalse(command.initializecommand("PLACE A,0,NSORTH"))

    def test_invalidcoorddatatype(self):
        command = Commands.PlaceCommand.PlaceCommand()
        self.assertFalse(command.initializecommand("PLACE 0,0,1"))

    def test_validatecommand(self):
        command = Commands.PlaceCommand.PlaceCommand()
        table = Table.Table(4,4)
        robot = Robot.Robot()
        command.initializecommand("PLACE 0,0,NORTH")
        self.assertTrue(command.validateinstruction(robot, table))

    def test_validatefalsecommand(self):
        command = Commands.PlaceCommand.PlaceCommand()
        table = Table.Table(4, 4)
        robot = Robot.Robot()
        command.initializecommand("PLACE 5,0,NORTH")
        self.assertFalse(command.validateinstruction(robot, table))

    def test_executecommand(self):
        command = Commands.PlaceCommand.PlaceCommand()
        table = Table.Table(4, 4)
        robot = Robot.Robot()
        command.initializecommand("PLACE 0,0,NORTH")
        command.executeinstruction(robot, table)
        self.assertTrue(table.currentrobot is robot)
        self.assertTrue(robot.width == 0)
        self.assertTrue(robot.height == 0)
        self.assertTrue(robot.direction == 1)


if __name__ == '__main__':
    unittest.main()
