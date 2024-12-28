from src.rover.position import Position
class Obstacle(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def is_at_position(self, x, y):
        return self.x == x and self.y == y