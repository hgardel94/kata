from command.move_command import MoveCommand
from command.turn_command import TurnCommand
from orientation.north_state import NorthState
from orientation.south_state import SouthState
from orientation.east_state import EastState
from orientation.west_state import WestState
from command.command import Command

class Rover:
    
    COMMAND_MAP = {
            'f': 'move_forward',
            'b': 'move_backward',
            'r': 'turn_right',
            'l': 'turn_left'
        }
    
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

    def execute_command(self, commands):
        for command in commands:
            method_name = self.COMMAND_MAP.get(command)
            action = self.COMMAND_MAP.get(command)
            if method_name:
                action = getattr(self, method_name)
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
