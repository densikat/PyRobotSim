from Commands import MoveCommand, PlaceCommand, ReportCommand, RightCommand, LeftCommand


class CommandFactory:

    _classes = {}
    _classes["MOVE"] = MoveCommand.MoveCommand
    _classes["PLACE"] = PlaceCommand.PlaceCommand
    _classes["REPORT"] = ReportCommand.ReportCommand
    _classes["RIGHT"] = RightCommand.RightCommand
    _classes["LEFT"] = LeftCommand.LeftCommand

    def __init__(self):
        pass

    @staticmethod
    def getclass(command):

        returnclass = None
        commandsplit = command.split(" ")
        commandname = commandsplit[0]

        if commandname in CommandFactory._classes:
            cmd = CommandFactory._classes[commandname]()
            cmd.initializecommand(command)
            return cmd
        return returnclass
