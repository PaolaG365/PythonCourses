from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player1 = TennisPlayer("Grisho", 26, 100)
        self.player2 = TennisPlayer("Peter", 23, 150)

    def test_correct_initialization(self):
        self.assertEqual("Grisho", self.player1.name)
        self.assertEqual(26, self.player1.age)
        self.assertEqual(100, self.player1.points)
        self.assertEqual([], self.player1.wins)

    def test_name_setter_raises_value_error_with_less_than_3_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.name = "hi"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_setter_raises_value_error_with_less_18(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 12
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win_with_not_won_yet_tournament(self):
        self.player1.add_new_win("Australia Open")
        self.assertEqual(["Australia Open"], self.player1.wins)

    def test_add_new_win_with_already_win_tournament(self):
        self.player1.wins.append("Australia Open")
        return_msg = self.player1.add_new_win("Australia Open")
        self.assertEqual("Australia Open has been already added to the list of wins!", return_msg)

    def test_less_than_with_first_player_having_less_points(self):
        return_msg = self.player1.__lt__(self.player2)
        self.assertEqual("Peter is a top seeded player and he/she is better than Grisho", return_msg)

    def test_less_than_with_first_player_having_more_points(self):
        return_msg = self.player2.__lt__(self.player1)
        self.assertEqual("Peter is a better player than Grisho", return_msg)

    def test_string_method_return_valid_info_with_no_wins(self):
        return_msg = self.player1.__str__()
        expected_msg = f"Tennis Player: Grisho\n" \
                       f"Age: 26\n" \
                       f"Points: 100.0\n" \
                       f"Tournaments won: "
        self.assertEqual(expected_msg, return_msg)

    def test_string_method_return_valid_info_with_wins(self):
        self.player1.add_new_win("Australia Open")
        self.player1.add_new_win("French Open")
        return_msg = self.player1.__str__()
        expected_msg = f"Tennis Player: Grisho\n" \
                       f"Age: 26\n" \
                       f"Points: 100.0\n" \
                       f"Tournaments won: Australia Open, French Open"
        self.assertEqual(expected_msg, return_msg)


if __name__ == '__main__':
    main()
