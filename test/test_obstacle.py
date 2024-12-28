import unittest
from src.planet.planet import Planet
from src.planet.obstacle import Obstacle

class TestObstacle(unittest.TestCase):
     def test_obstacle(self):
        self.obstacle = Obstacle(5, 5)
        mars = Planet(10, 10)
        mars.add_obstacle(self.obstacle)
        self.assertTrue(mars.check_for_obstacles(5, 5))
        self.assertFalse(mars.check_for_obstacles(5, 6))

if __name__ == '__main__':
    unittest.main()  