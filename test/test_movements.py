import unittest
from src.planet.planet import Planet
from src.rover.rover import Rover
from src.planet.obstacle import Obstacle  

class TestMovements(unittest.TestCase):    
    
    def test_move_forward(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.rover.move("f")
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 1)
        self.assertEqual(self.rover.direction, "N")
    
    def test_move_forward_obstacle_exception(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.obstacle = Obstacle(0, 1)
        self.mars.add_obstacle(self.obstacle)
        with self.assertRaises(Exception) as context:
            self.rover.simulate_next_move("f")
        self.assertFalse("Obstacle detected at position:(0, 1). Movement not executed." in str(context.exception))    
    
    def test_move_back(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.rover.move("b")
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 9)
        self.assertEqual(self.rover.direction, "N")
    
    def test_move_back_obstacle_exception(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.obstacle = Obstacle(0, 9)
        self.mars.add_obstacle(self.obstacle)
        with self.assertRaises(Exception) as context:
            self.rover.simulate_next_move("b")
        self.assertFalse("Obstacle detected at position:(0, 9). Movement not executed." in str(context.exception))
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.direction, "N")
        
    
    
    def test_turn_left(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.rover.move("l")
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.direction, "O")
    
    def test_turn_right(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.rover.move("r")
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.direction, "E")
        

if __name__ == '__main__':
    unittest.main()