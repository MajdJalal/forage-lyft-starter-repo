from abc import ABC

from engine import engine


class CapuletEngine(ABC, engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    #majd explanation : current milage represnts milage taken since the manifacturing 
    #last service milage represets at what milage the last service happened to the engin 
