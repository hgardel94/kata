import unittest
from rover import Rover
from orientation.north_state import NorthState
from orientation.south_state import SouthState
from orientation.east_state import EastState
from orientation.west_state import WestState
from planet import Planet

class TestRover(unittest.TestCase):
    
    def setUp(self):
        self.mars = Planet(10, 10)
        self.rover = Rover([0, 0], NorthState(), self.mars)
        self.mars.add_obstacle([0,2])
        self.mars.add_obstacle([0,7])

    def test_move_forward(self):
        
        self.rover.execute_command(['f'])
        self.assertEqual(self.rover.position, [0, 1])  
        
    def test_move_backward(self):
        self.rover.execute_command(['b'])
        self.assertEqual(self.rover.position, [0, 9])
    
    def test_turn_right(self):
        self.rover.execute_command(['r'])
        self.assertIsInstance(self.rover.orientation, EastState)
        
    def test_turn_right_x2(self):
        self.rover.execute_command(['r', 'r'])
        self.assertIsInstance(self.rover.orientation, SouthState)    
    
    def test_turn_left(self):
        self.rover.execute_command(['l'])
        self.assertIsInstance(self.rover.orientation, WestState)
    
    def test_turn_left_x2(self):
        self.rover.execute_command(['l', 'l'])
        self.assertIsInstance(self.rover.orientation, SouthState)
        
    
    def test_move_forward_with_obstacle(self):
        self.rover.execute_command(['f', 'f'])
        self.assertEqual(self.rover.position, [0,1])
        
    def test_move_backward_with_obstacle(self):
        self.rover.execute_command(['b', 'b', 'b'])
        self.assertEqual(self.rover.position, [0,8])
        

if __name__ == '__main__':
    unittest.main()
