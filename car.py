from abc import ABC, abstractmethod
from engine.serviceable import serviceable


class Car(serviceable):
    '''def __init__(self, last_service_date):
        self.last_service_date = last_service_date #date of last service of the car 
    '''
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    @abstractmethod
    def needs_service(self):
        pass
