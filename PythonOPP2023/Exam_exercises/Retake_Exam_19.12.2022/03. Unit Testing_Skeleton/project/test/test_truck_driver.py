from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self):
        self.truck_driver1 = TruckDriver("George", 12)

    def test_correct_initialization(self):
        self.assertEqual("George", self.truck_driver1.name)
        self.assertEqual(12, self.truck_driver1.money_per_mile)
        self.assertEqual({}, self.truck_driver1.available_cargos)
        self.assertEqual(0, self.truck_driver1.earned_money)
        self.assertEqual(0, self.truck_driver1.miles)

    def test_money_setter_with_negatives_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver1.earned_money = -1
        self.assertEqual("George went bankrupt.", str(ve.exception))

    def test_going_bankrupt_while_driving(self):
        self.truck_driver1.money_per_mile = 0.1
        self.truck_driver1.add_cargo_offer("location1", 1000)
        with self.assertRaises(ValueError) as ve:
            self.truck_driver1.drive_best_cargo_offer()
        self.assertEqual("George went bankrupt.", str(ve.exception))

    def test_add_non_existing_cargo_offer(self):
        return_msg = self.truck_driver1.add_cargo_offer("location1", 100)
        expected_msg = "Cargo for 100 to location1 was added as an offer."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual({"location1": 100}, self.truck_driver1.available_cargos)

    def test_adding_existing_cargo_offer_raises_exception(self):
        self.truck_driver1.add_cargo_offer("location1", 100)
        with self.assertRaises(Exception) as ex:
            self.truck_driver1.add_cargo_offer("location1", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_driving_best_cargo_offer_250_miles_away(self):
        self.truck_driver1.add_cargo_offer("location1", 250)
        return_msg = self.truck_driver1.drive_best_cargo_offer()
        expected_msg = "George is driving 250 to location1."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual(2_980, self.truck_driver1.earned_money)
        self.assertEqual(250, self.truck_driver1.miles)

    def test_driving_best_cargo_offer_250_miles_away_with_two_locations(self):
        self.truck_driver1.add_cargo_offer("location1", 250)
        self.truck_driver1.add_cargo_offer("location2", 25)
        return_msg = self.truck_driver1.drive_best_cargo_offer()
        expected_msg = "George is driving 250 to location1."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual(2_980, self.truck_driver1.earned_money)
        self.assertEqual(250, self.truck_driver1.miles)

    def test_driving_best_cargo_offer_1000_miles_away(self):
        self.truck_driver1.add_cargo_offer("location1", 1000)
        return_msg = self.truck_driver1.drive_best_cargo_offer()
        expected_msg = "George is driving 1000 to location1."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual(11_875, self.truck_driver1.earned_money)
        self.assertEqual(1000, self.truck_driver1.miles)

    def test_driving_best_cargo_offer_1500_miles_away(self):
        self.truck_driver1.add_cargo_offer("location1", 1500)
        return_msg = self.truck_driver1.drive_best_cargo_offer()
        expected_msg = "George is driving 1500 to location1."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual(17_335, self.truck_driver1.earned_money)
        self.assertEqual(1500, self.truck_driver1.miles)

    def test_driving_best_cargo_offer_10_000_miles_away(self):
        self.truck_driver1.add_cargo_offer("location1", 10_000)
        return_msg = self.truck_driver1.drive_best_cargo_offer()
        expected_msg = "George is driving 10000 to location1."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual(108_250, self.truck_driver1.earned_money)
        self.assertEqual(10_000, self.truck_driver1.miles)

    def test_driving_best_cargo_offer_with_no_offers(self):
        return_msg = self.truck_driver1.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", return_msg)

    def test_represent_methods_return_valid_info(self):
        return_msg = self.truck_driver1.__repr__()
        self.assertEqual("George has 0 miles behind his back.", return_msg)


if __name__ == '__main__':
    main()
