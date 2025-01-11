from command.move_command import MoveCommand
from command.turn_command import TurnCommand
from orientation.north_state import NorthState
from orientation.south_state import SouthState
from orientation.east_state import EastState
from orientation.west_state import WestState

class Rover:
    
    ORIENTATION_CLASSES = {
        'NorthState': NorthState,
        'SouthState': SouthState,
        'EastState': EastState,
        'WestState': WestState
    }

    def __init__(self, position, orientation, planet):
        self.position = position
        self.orientation = orientation
        self.planet = planet
        self.command_history = []
        self.command_map = {
            'f': self.move_forward,
            'b': self.move_backward,
            'r': self.turn_right,
            'l': self.turn_left
        }

    def execute_command(self, commands):
        for command in commands:
            action = self.command_map.get(command)
            if action:
                action()

    def undo_last_command(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()

    def move_forward(self):
        command = MoveCommand(self, self.orientation.move_forward)
        if command.execute():
            self.command_history.append(command)

    def move_backward(self):
        command = MoveCommand(self, self.orientation.move_backward)
        if command.execute():
            self.command_history.append(command)

    def turn_left(self):
        new_orientation_class_name = self.orientation.turn_left()
        new_orientation_class = self.ORIENTATION_CLASSES[new_orientation_class_name]
        new_orientation_instance = new_orientation_class()
        command = TurnCommand(self, new_orientation_instance)
        if command.execute():
            self.command_history.append(command)

    def turn_right(self):
        new_orientation_class_name = self.orientation.turn_right()
        new_orientation_class = self.ORIENTATION_CLASSES[new_orientation_class_name]
        new_orientation_instance = new_orientation_class()
        command = TurnCommand(self, new_orientation_instance)
        if command.execute():
            self.command_history.append(command)
