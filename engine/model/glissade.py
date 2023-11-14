from datetime import datetime
from car import Car
from engine.Engines.willoughby_engine import WilloughbyEngine


class Glissade(Car):
    def __init__(self, engin, battery, tire):
        super.__init__(engin, battery, tire)
    
    def needs_service(self):
        return self.engin.needs_service() or self.battery.needs_service()or self.tire.need_service()
