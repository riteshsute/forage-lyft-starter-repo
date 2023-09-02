from .car_engine import CarEngine

class Glissade(CarEngine):
    def needs_service(self):
        return self.engine_should_be_serviced()
