from datetime import datetime
from car import Car
from engine.Engines.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, engin, battery, tire):
        super.__init__(engin, battery, tire)
    
    def needs_service(self):
        return self.engin.needs_service() or self.battery.needs_service() or self.tire.need_service()
    