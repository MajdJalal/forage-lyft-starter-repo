from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope():
    #all dependencies 
    def __init__(self, engin, battery):
        self.engin = engin
        self.battery = battery
    
    def needs_service(self):
        return self.engin.needs_service() or self.battery.needs_service()
   