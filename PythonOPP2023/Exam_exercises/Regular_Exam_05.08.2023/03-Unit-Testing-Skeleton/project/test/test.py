from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.second_hand_car = SecondHandCar("Test model", "Test type", 10_000, 3000)

    def test_valid_initialization(self):
        self.assertEqual("Test model", self.second_hand_car.model)
        self.assertEqual("Test type", self.second_hand_car.car_type)
        self.assertEqual(10_000, self.second_hand_car.mileage)
        self.assertEqual(3000, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_invalid_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.second_hand_car.price = 0.2
        self.assertEqual("Price should be greater than 1.0!", str(ex.exception))

    def test_invalid_mileage_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.second_hand_car.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ex.exception))

    def test_unsuccessful_change_of_discount_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.second_hand_car.set_promotional_price(3200)
        self.assertEqual("You are supposed to decrease the price!", str(ex.exception))

    def test_successful_change_of_discount_price(self):
        return_msg = self.second_hand_car.set_promotional_price(2600)
        self.assertEqual("The promotional price has been successfully set.", return_msg)
        self.assertEqual(2600, self.second_hand_car.price)

    def test_not_possible_repair(self):
        return_msg = self.second_hand_car.need_repair(2000, "repair notes")
        self.assertEqual("Repair is impossible!", return_msg)

    def test_valid_repairs_done(self):
        return_msg = self.second_hand_car.need_repair(1000, "repair notes")
        self.assertEqual("Price has been increased due to repair charges.", return_msg)
        self.assertEqual(4000, self.second_hand_car.price)
        self.assertEqual(["repair notes"], self.second_hand_car.repairs)

    def test_greater_than_method(self):
        another_second_hand_car = SecondHandCar("Other model", "Test type", 5_000, 4000)
        self.assertFalse(self.second_hand_car > another_second_hand_car)
        self.assertTrue(self.second_hand_car < another_second_hand_car)

    def test_not_same_type_cars_cannot_be_compared(self):
        another_second_hand_car = SecondHandCar("Other model", "Other type", 5_000, 4000)
        return_msg = self.second_hand_car > another_second_hand_car
        self.assertEqual("Cars cannot be compared. Type mismatch!", return_msg)

    def test_string_method_returns_valid_info(self):
        return_msg = self.second_hand_car.__str__()
        expected_msg = "Model Test model | Type Test type | Milage 10000km\n"\
                       "Current price: 3000.00 | Number of Repairs: 0"
        self.assertEqual(expected_msg, return_msg)


if __name__ == '__main__':
    main()
