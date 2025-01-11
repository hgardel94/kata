from command.command import Command

class MoveCommand(Command):
    def __init__(self, rover, move_method):
        super().__init__(rover)
        self.move_method = move_method
        self.previous_position = None

    def execute(self):
        self.previous_position = self.rover.position.copy()
        new_position = self.move_method(self.rover.position)
        wrapped_position = self.rover.planet.wrap_position(new_position)

        if self.rover.planet.is_obstacle(wrapped_position):
            print("¡Obstacle detected!")
            return False

        self.rover.position = wrapped_position
        return True

    def undo(self):
        self.rover.position = self.previous_position
