from Commands import MoveCommand, PlaceCommand, ReportCommand, RightCommand, LeftCommand, ExitCommand


class CommandFactory:

    _classes = {
        "MOVE": MoveCommand.MoveCommand,
        "PLACE": PlaceCommand.PlaceCommand,
        "REPORT": ReportCommand.ReportCommand,
        "RIGHT": RightCommand.RightCommand,
        "LEFT": LeftCommand.LeftCommand,
        "EXIT": ExitCommand.ExitCommand
    }

    def __init__(self):
        pass

    @staticmethod
    def getclass(command):

        returnclass = None
        commandsplit = command.split(" ")
        commandname = commandsplit[0]

        # If the command is in our _classes dict then return command object
        if commandname in CommandFactory._classes:
            cmd = CommandFactory._classes[commandname]()
            cmd.initializecommand(command)
            return cmd
        return returnclass
