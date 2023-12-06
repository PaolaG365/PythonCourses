from unittest import TestCase, main
from car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car("test car", "test model", 5, 60)

    def test_initialization_with_correct_data(self):
        self.assertEqual("test car", self.car.make)
        self.assertEqual("test model", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raises_exception_with_empty_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises_exception_with_empty_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_with_less_than_0_data_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_refuel_with_less_max_capacity_valid_data(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refuel_refuel_with_more_tan_max_capacity_valid_data(self):
        self.car.refuel(70)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_refuel_with_0_or_less_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_with_enough_fuel_to_drive(self):
        self.car.fuel_amount = 30
        self.car.drive(20)
        self.assertEqual(29, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_to_drive(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
