from abc import ABC, ABCMeta, abstractmethod
from Robot import Robot
from Table import Table


class Command(ABC):

    def __init__(self,commandname):
        self.commandname = commandname

    @abstractmethod
    def initializecommand(self, command):
        pass

    @abstractmethod
    def validateinstruction(self, robot, table):
        pass

    @abstractmethod
    def executeinstruction(self, robot, table):
        pass


