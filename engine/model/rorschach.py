from datetime import datetime
from .car_engine import CarEngine

class Rorschach(CarEngine):
    def needs_service(self):
        return (
            self.engine_should_be_serviced()
            or self.last_service_date.replace(year=self.last_service_date.year + 4) < datetime.today().date()
        )
