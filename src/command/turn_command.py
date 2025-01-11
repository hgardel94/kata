from command.command import Command

class TurnCommand(Command):
    def __init__(self, rover, new_orientation):
        super().__init__(rover)
        self.new_orientation = new_orientation
        self.previous_orientation = None

    def execute(self):
        self.previous_orientation = self.rover.orientation
        self.rover.orientation = self.new_orientation
        return True

    def undo(self):
        self.rover.orientation = self.previous_orientation
