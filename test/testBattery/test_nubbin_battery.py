import unittest
from datetime import date
import sys
sys.path.append('C:\\Users\\PC\\Desktop\\forage-lyft-starter-repo')
from engine.Batteries.NubbinBattery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery( last_service_date, current_date,)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()