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

class Position:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Obstacle(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def is_at_position(self, x, y):
        return self.x == x and self.y == y

class Obstacle_Exception(Exception):
    def __init__(self, x, y):
        super().__init__(f"Obstacle detected at position:({x}, {y}). Movement not executed.")
        self.x = x
        self.y = y  

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

class Rover(Position):
    DIRECTIONS = ["N", "E", "S", "O"]
    
    def __init__(self, x, y, direction, planet):
        super().__init__(x, y)
        self.direction = direction
        self.planet = planet
        self.movements = Movements(self)

    def move(self, commands):
        for command in commands:
            command = command.lower()
            try: 
                if self.movements.simulate_next_move(command): 
                    self.movements.execute_move(command) 
            
            except Obstacle_Exception as e: 
                print(e) 
                break
                

    def show_position(self):
        print(f"The Rover is at position: ({self.x}, {self.y}), facing {self.direction}")


        

