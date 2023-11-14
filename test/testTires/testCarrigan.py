import unittest
from engine.Tires import Carrigan

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        arr = [0, 0, 0.1, 0.9]
        tire = Carrigan(arr)
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        arr = [0.8, 0.7, 0, 0.4]
        tire = Carrigan(arr)
        self.assertFalse(tire.needs_service())


