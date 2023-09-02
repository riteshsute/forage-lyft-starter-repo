import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()
    
    def create_car(self, last_service_years_ago, current_mileage, last_service_mileage):
        last_service_date = self.today.replace(year=self.today.year - last_service_years_ago)
        return last_service_date, current_mileage, last_service_mileage

class TestCalliope(TestVehicle):
    def test_battery_should_be_serviced(self):
        args = self.create_car(3, 0, 0)
        car = Calliope(*args)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        args = self.create_car(1, 0, 0)
        car = Calliope(*args)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        args = self.create_car(0, 30001, 0)
        car = Calliope(*args)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        args = self.create_car(0, 30000, 0)
        car = Calliope(*args)
        self.assertFalse(car.needs_service())


class TestGlissade(TestVehicle):
    def test_battery_should_be_serviced(self):
        args = self.create_car(3, 0, 0)
        car = Glissade(*args)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        args = self.create_car(1, 0, 0)
        car = Glissade(*args)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        args = self.create_car(0, 30001, 0)
        car = Glissade(*args)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        args = self.create_car(0, 30000, 0)
        car = Glissade(*args)
        self.assertFalse(car.needs_service())


class TestPalindrome(TestVehicle):
    def test_battery_should_be_serviced(self):
        args = self.create_car(3, 0, 0)
        car = Palindrome(*args)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        args = self.create_car(1, 0, 0)
        car = Palindrome(*args)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        args = self.create_car(0, 30001, 0)
        car = Palindrome(*args)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        args = self.create_car(0, 30000, 0)
        car = Palindrome(*args)
        self.assertFalse(car.needs_service())


class TestRorschach(TestVehicle):
    def test_battery_should_be_serviced(self):
        args = self.create_car(3, 0, 0)
        car = Rorschach(*args)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        args = self.create_car(1, 0, 0)
        car = Rorschach(*args)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        args = self.create_car(0, 30001, 0)
        car = Rorschach(*args)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        args = self.create_car(0, 30000, 0)
        car = Rorschach(*args)
        self.assertFalse(car.needs_service())


class TestThovex(TestVehicle):
    def test_battery_should_be_serviced(self):
        args = self.create_car(3, 0, 0)
        car = Thovex(*args)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        args = self.create_car(1, 0, 0)
        car = Thovex(*args)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        args = self.create_car(0, 30001, 0)
        car = Thovex(*args)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        args = self.create_car(0, 30000, 0)
        car = Thovex(*args)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
