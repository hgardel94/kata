class Planet:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.obstacles = []

    def end_of_planet(self, x, y):
        return x % self.width, y % self.height

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def check_for_obstacles(self, x, y):
        for obstacle in self.obstacles:
            if obstacle.is_at_position(x, y):
                return True
        return False