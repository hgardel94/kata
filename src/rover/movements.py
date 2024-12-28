from src.exceptions import Obstacle_Exception
class Movements:
    DIRECTIONS = ["N", "E", "S", "O"]
    
    def __init__(self, rover):
        self.rover = rover

    def simulate_next_move(self, command):
        new_x, new_y = self.rover.x, self.rover.y

        if command == "f":
            new_x, new_y = self.calculate_forward(new_x, new_y)
        if command == "b":
            new_x, new_y = self.calculate_back(new_x, new_y)
        if command == "l" or command == "r":    
            return True

        new_x, new_y = self.rover.planet.end_of_planet(new_x, new_y)

        if self.rover.planet.check_for_obstacles(new_x, new_y):
            raise Obstacle_Exception(new_x, new_y)
        
        return True
    
    def execute_move(self, command):
        if command == "f":
            self.rover.x, self.rover.y = self.calculate_forward(self.rover.x, self.rover.y)
        if command == "b":
            self.rover.x, self.rover.y = self.calculate_back(self.rover.x, self.rover.y)
        if command == "l":
            self.turn_left()
        if command == "r":
            self.turn_right()

        self.rover.x, self.rover.y = self.rover.planet.end_of_planet(self.rover.x, self.rover.y)
    
    def calculate_forward(self, x, y):
        if self.rover.direction == "N":
            y += 1
        if self.rover.direction == "S":
            y -= 1
        if self.rover.direction == "E":
            x += 1
        if self.rover.direction == "O":
            x -= 1
        return x, y
    
    def calculate_back(self, x, y):
        if self.rover.direction == "N":
            y -= 1
        if self.rover.direction == "S":
            y += 1
        if self.rover.direction == "E":
            x -= 1
        if self.rover.direction == "O":
            x += 1
        return x, y
    
    def turn_left(self):
        idx = (self.DIRECTIONS.index(self.rover.direction) - 1) % 4
        self.rover.direction = self.DIRECTIONS[idx]
    
    def turn_right(self):
        idx = (self.DIRECTIONS.index(self.rover.direction) + 1) % 4
        self.rover.direction = self.DIRECTIONS[idx]
