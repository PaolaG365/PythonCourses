from collections import deque

from project.railway_station import RailwayStation
from unittest import TestCase, main


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway_station = RailwayStation("RS Varna")

    def test_correct_initialization(self):
        self.assertEqual("RS Varna", self.railway_station.name)
        self.assertEqual(deque([]), self.railway_station.arrival_trains)
        self.assertEqual(deque([]), self.railway_station.departure_trains)

    def test_name_setter_with_less_than_four_symbols_len_string(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "RSS"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_adding_arriving_trains_in_deq(self):
        self.railway_station.new_arrival_on_board("Sofia-Varna-10h-delay")
        self.assertEqual(deque(["Sofia-Varna-10h-delay"]), self.railway_station.arrival_trains)

    def test_train_has_arrived_with_wrong_train_trying_to_arrive(self):
        self.railway_station.new_arrival_on_board("Sofia-Varna-10h-delay")
        return_msg = self.railway_station.train_has_arrived("StaraZagora-Varna-3h-delay")
        self.assertEqual("There are other trains to arrive before StaraZagora-Varna-3h-delay.", return_msg)

    def test_train_has_arrived_with_valid_train_trying_to_arrive(self):
        self.railway_station.new_arrival_on_board("Sofia-Varna-10h-delay")
        return_msg = self.railway_station.train_has_arrived("Sofia-Varna-10h-delay")
        expected_msg = "Sofia-Varna-10h-delay is on the platform and will leave in 5 minutes."
        self.assertEqual(expected_msg, return_msg)
        self.assertEqual(deque(["Sofia-Varna-10h-delay"]), self.railway_station.departure_trains)
        self.assertEqual(deque([]), self.railway_station.arrival_trains)

    def test_train_has_arrived_with_no_arriving_trains_in_deq(self):
        with self.assertRaises(IndexError) as ie:
            self.railway_station.train_has_arrived("Sofia-Varna-10h-delay")
        self.assertEqual("pop from an empty deque", str(ie.exception))

    def test_train_has_left_for_real_unbelievable(self):
        self.railway_station.new_arrival_on_board("Sofia-Varna-10h-delay")
        self.railway_station.train_has_arrived("Sofia-Varna-10h-delay")
        self.assertTrue(self.railway_station.train_has_left("Sofia-Varna-10h-delay"))
        self.assertEqual(deque([]), self.railway_station.arrival_trains)
        self.assertEqual(deque([]), self.railway_station.departure_trains)

    def test_train_has_left_with_not_yet_left_train_ofc(self):
        self.railway_station.new_arrival_on_board("Sofia-Varna-10h-delay")
        self.railway_station.new_arrival_on_board("StaraZagora-Varna-3h-delay")
        self.railway_station.train_has_arrived("Sofia-Varna-10h-delay")
        self.railway_station.train_has_arrived("StaraZagora-Varna-3h-delay")
        self.assertFalse(self.railway_station.train_has_left("StaraZagora-Varna-3h-delay"))
        self.assertEqual(deque([]), self.railway_station.arrival_trains)
        self.assertEqual(deque(["Sofia-Varna-10h-delay",
                                "StaraZagora-Varna-3h-delay"]), self.railway_station.departure_trains)


if __name__ == '__main__':
    main()
