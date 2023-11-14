import unittest

import sys
sys.path.append('C:\\Users\\PC\\Desktop\\forage-lyft-starter-repo')
from engine.Tires.Octoprime import Octoprime

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        arr = [1, 0.9, 0.1, 1]
        tire = Octoprime()
        self.assertTrue(tire.needs_service(arr))
    
    def test_tire_should_not_be_serviced(self):
        arr = [0.8, 0.7, 0, 0.4]
        tire = Octoprime()
        self.assertFalse(tire.needs_service(arr))

if __name__ == '__main__':
    unittest.main()