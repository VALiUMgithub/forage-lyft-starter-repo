import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()
        self.last_service_mileage = 0

    def create_car(self, last_service_date, current_mileage):
        raise NotImplementedError

    def test_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        current_mileage = 0

        car = self.create_car(last_service_date, current_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        current_mileage = 0

        car = self.create_car(last_service_date, current_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = self.today
        current_mileage = self.last_service_mileage + 30001

        car = self.create_car(last_service_date, current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = self.today
        current_mileage = self.last_service_mileage + 30000

        car = self.create_car(last_service_date, current_mileage)
        self.assertFalse(car.needs_service())


class TestCalliope(CarTestCase):
    def create_car(self, last_service_date, current_mileage):
        return Calliope(last_service_date, current_mileage, self.last_service_mileage)


class TestGlissade(CarTestCase):
    def create_car(self, last_service_date, current_mileage):
        return Glissade(last_service_date, current_mileage, self.last_service_mileage)


class TestPalindrome(CarTestCase):
    def create_car(self, last_service_date, current_mileage):
        warning_light_is_on = False
        return Palindrome(last_service_date, warning_light_is_on)


class TestRorschach(CarTestCase):
    def create_car(self, last_service_date, current_mileage):
        return Rorschach(last_service_date, current_mileage, self.last_service_mileage)


class TestThovex(CarTestCase):
    def create_car(self, last_service_date, current_mileage):
        return Thovex(last_service_date, current_mileage, self.last_service_mileage)


if __name__ == '__main__':
    unittest.main()
