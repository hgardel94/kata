import unittest
from kata_rover import Planet, Rover, Obstacle, Movements, Obstacle_Exception

class TestPlanet(unittest.TestCase):
    def test_create_planet(self):
        mars = Planet(10, 10)
        self.assertEqual(mars.width, 10)
        self.assertEqual(mars.height, 10)
    
    def test_end_of_planet(self):
        mars = Planet(10, 10)
        self.assertEqual(mars.end_of_planet(10, 10), (0, 0))
        self.assertEqual(mars.end_of_planet(11, 11), (1, 1))
        self.assertEqual(mars.end_of_planet(-2, 4), (8, 4))
        
class TestObstacle(unittest.TestCase):
     def test_obstacle(self):
        self.obstacle = Obstacle(5, 5)
        mars = Planet(10, 10)
        mars.add_obstacle(self.obstacle)
        self.assertTrue(mars.check_for_obstacles(5, 5))
        self.assertFalse(mars.check_for_obstacles(5, 6))
    
class TestRover(unittest.TestCase):
    def test_create_rover(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.direction, "N")
        self.assertEqual(self.rover.planet, self.mars)

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
