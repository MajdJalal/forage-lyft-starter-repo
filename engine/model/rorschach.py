from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def __init__(self, engin, battery):
        self.engin = engin
        self.battery = battery
    
    def needs_service(self):
        return self.engin.needs_service() or self.battery.needs_service()
