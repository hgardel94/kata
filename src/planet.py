# planet.py
class Planet:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []

    def add_obstacle(self, position):
        self.obstacles.append(position)

    def is_obstacle(self, position):
        return position in self.obstacles


    def wrap_position(self, position):
        return [position[0] % self.width, position[1] % self.height]