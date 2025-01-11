from orientation.orientation_state import OrientationState

class WestState(OrientationState):
    def move_forward(self, position):
        return [position[0] - 1, position[1]]

    def move_backward(self, position):
        return [position[0] + 1, position[1]]

    def turn_left(self):
        return 'SouthState'

    def turn_right(self):
        return 'NorthState'
