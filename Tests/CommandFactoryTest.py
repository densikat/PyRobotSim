import unittest
from unittest import TestCase
from Commands import CommandFactory, MoveCommand

__author__ = 'David Ensikat'
__project__ = 'PyRobotSim'


class CommandFactoryTest(TestCase):
    def test_movecommand(self):
        movecommand = CommandFactory.CommandFactory.getclass("MOVE")
        self.assertEqual(type(movecommand),MoveCommand.MoveCommand)


if __name__ == '__main__':
    unittest.main()