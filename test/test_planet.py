import unittest 
from src.planet.planet import Planet
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
        
        
if __name__ == "__main__":
    unittest.main()