import unittest
from src.rover.rover import Rover
from src.planet.planet import Planet

class TestRover(unittest.TestCase):
    def test_create_rover(self):
        self.mars = Planet(10, 10)
        self.rover = Rover(0, 0, "N", self.mars)
        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 0)
        self.assertEqual(self.rover.direction, "N")
        self.assertEqual(self.rover.planet, self.mars)

if __name__ == '__main__':
    unittest.main()