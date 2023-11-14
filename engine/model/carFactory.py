
from engine.Batteries.NubbinBattery import NubbinBattery
from engine.Batteries.SpindlerBattery import SpindlerBattery
from engine.Engines.capulet_engine import CapuletEngine
from engine.Engines.sternman_engine import SternmanEngine
from engine.Engines.willoughby_engine import WilloughbyEngine 

class carFactory():
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = car(engin, battery)
        return car
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = car(engin, battery)
        return car
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engin = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = car(engin, battery)
        return car
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = car(engin, battery)
        return car
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = car(engin, battery)
        return car
