from orientation.orientation_state import OrientationState

class SouthState(OrientationState):
    def move_forward(self, position):
        return [position[0], position[1] - 1]

    def move_backward(self, position):
        return [position[0], position[1] + 1]

    def turn_left(self):
        return 'EastState'

    def turn_right(self):
        return 'WestState'

    def turn_right(self):
        return 'WestState'  
