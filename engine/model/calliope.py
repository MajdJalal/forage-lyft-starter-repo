from datetime import datetime
from car import Car

from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    #all dependencies 
    def __init__(self, engin, battery):
        super.__init__(engin, battery)
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
   