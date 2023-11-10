from Battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > 2 and self.current_date.month > self.last_service_date.month and self.current_date.days > self.last_service_date.days