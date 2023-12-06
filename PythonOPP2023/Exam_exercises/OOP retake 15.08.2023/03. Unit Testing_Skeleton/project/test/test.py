from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.sample_trip = Trip(1000, 1, False)

    def test_initialization(self):
        self.assertEqual(1000, self.sample_trip.budget)
        self.assertEqual(1, self.sample_trip.travelers)
        self.assertEqual(False, self.sample_trip.is_family)
        self.assertEqual({}, self.sample_trip.booked_destinations_paid_amounts)

    def test_travelers_setter_raises_value_error_with_0_travelers(self):
        with self.assertRaises(ValueError) as exc:
            self.sample_trip.travelers = 0
        self.assertEqual("At least one traveler is required!", str(exc.exception))

    def test_is_family_setter_with_2_or_more_tr_returns_value(self):
        self.sample_trip.travelers = 2
        self.sample_trip.is_family = "asd"
        self.assertEqual("asd", self.sample_trip.is_family)

    def test_is_family_with_value_and_one_traveler(self):
        self.sample_trip.is_family = "asd"
        self.assertEqual(False, self.sample_trip.is_family)

    def test_booking_a_trip_to_destination_not_found(self):
        return_msg = self.sample_trip.book_a_trip("Japan")
        self.assertEqual("This destination is not in our offers, please choose a new one!", return_msg)

    def test_booking_a_valid_trip_to_destination_with_single_person_with_not_enough_budget(self):
        return_msg = self.sample_trip.book_a_trip("Brazil")
        self.assertEqual("Your budget is not enough!", return_msg)

    def test_booking_a_valid_trip_to_destination__single_person_enough_budget(self):
        return_msg = self.sample_trip.book_a_trip("Bulgaria")
        expected_msg = f"Successfully booked destination Bulgaria! Your budget left is 500.00"
        self.assertEqual(500, self.sample_trip.budget)
        self.assertEqual({"Bulgaria": 500}, self.sample_trip.booked_destinations_paid_amounts)
        self.assertEqual(expected_msg, return_msg)

    def test_book_a_trip_with_family(self):
        sample_family = Trip(2000, 3, True)
        return_msg = sample_family.book_a_trip("Bulgaria")
        expected_msg = f"Successfully booked destination Bulgaria! Your budget left is 650.00"
        self.assertEqual(650, sample_family.budget)
        self.assertEqual({"Bulgaria": 1350}, sample_family.booked_destinations_paid_amounts)
        self.assertEqual(expected_msg, return_msg)

    def test_booking_status_with_empty_booked_destinations(self):
        return_msg = self.sample_trip.booking_status()
        self.assertEqual("No bookings yet. Budget: 1000.00", return_msg)

    def test_booking_status_with_two_actually_booked_destinations_and_sorting(self):
        self.sample_trip.budget = 10000
        self.sample_trip.book_a_trip("Bulgaria")
        self.sample_trip.book_a_trip("New Zealand")
        return_msg = self.sample_trip.booking_status()
        expected_msg = ("Booked Destination: Bulgaria\nPaid Amount: 500.00\n"
                        "Booked Destination: New Zealand\nPaid Amount: 7500.00\n"
                        "Number of Travelers: 1\nBudget Left: 2000.00")
        self.assertEqual(expected_msg, return_msg)


if __name__ == '__main__':
    main()
