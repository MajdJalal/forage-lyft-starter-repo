
from engine.NubbinBattery import NubbinBattery
from engine.SpindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine 

class carFactory():
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_mileage)
        car = car(engin, battery)
        return car
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_mileage)
        car = car(engin, battery)
        return car
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = SternmanEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_mileage)
        car = car(engin, battery)
        return car
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_mileage)
        car = car(engin, battery)
        return car
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engin = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_mileage)
        car = car(engin, battery)
        return car
