class Obstacle_Exception(Exception):
    def __init__(self, x, y):
        super().__init__(f"Obstacle detected at position:({x}, {y}). Movement not executed.")
        self.x = x
        self.y = y