from abc import ABC, abstractmethod

class OrientationState(ABC):
    @abstractmethod
    def move_forward(self, position):
        pass

    @abstractmethod
    def move_backward(self, position):
        pass

    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass
