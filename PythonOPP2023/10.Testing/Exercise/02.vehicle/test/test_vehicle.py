from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(150, 200)

    def test_init_vehicle(self):
        self.assertEqual(150, self.car.fuel)
        self.assertEqual(150, self.car.capacity)
        self.assertEqual(200, self.car.horse_power)
        self.assertEqual(self.car.fuel_consumption, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_enough_fuel(self):
        self.car.drive(30)
        self.assertEqual(112.5, self.car.fuel)

    def test_drive_without_enough_fuel_to_destination(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(150)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refueling_with_less_than_max_capacity(self):
        self.car.fuel = 0
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel)

    def test_refueling_more_than_max_capacity_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(150)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_method_return(self):
        expected_msg = "The vehicle has 200 horse power with 150 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_msg, self.car.__str__())


if __name__ == '__main__':
    main()
