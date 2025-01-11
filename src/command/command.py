class Command:
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError
