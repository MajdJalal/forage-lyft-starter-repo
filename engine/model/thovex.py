from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, engin, battery):
        super.__init__(engin, battery)
    
    def needs_service(self):
        return self.engin.needs_service() or self.battery.needs_service()
    