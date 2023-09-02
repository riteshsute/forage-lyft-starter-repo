from datetime import datetime

class CarEngine:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return (
            self.current_mileage - self.last_service_mileage >= 30000
            or self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()
        )