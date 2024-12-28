from src.rover.position import Position
from src.rover.movements import Movements
from src.exceptions.obstacle_exception import Obstacle_Exception
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