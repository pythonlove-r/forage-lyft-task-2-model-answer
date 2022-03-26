import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = CapuletEngine(0, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date()-5)


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = CapuletEngine(0, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date()-1)


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(30001, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())


    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(1, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = WilloughbyEngine(0, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date()-5)


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = WilloughbyEngine(0, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date()-1)


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(600001, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(1, 0)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())


        car = Car(engine, battery)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date()-5)
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date()-1)
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(!warning_light_is_on)
        battery = SpindlerBattery(datetime.today().date(), datetime.today().date())
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = WilloughbyEngine(0,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date()-5)
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = WilloughbyEngine(0,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date()-3)
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(60001,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date())
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(1,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date())
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = CapuletEngine(0,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date()-5)
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = CapuletEngine(0,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date()-3)
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(30001,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date())
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(1,0)
        battery = NubbinBattery(datetime.today().date(), datetime.today().date())
        
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()
