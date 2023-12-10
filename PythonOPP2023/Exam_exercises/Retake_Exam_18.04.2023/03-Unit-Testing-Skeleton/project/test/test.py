from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.sample_robot = Robot("1x23", "Humanoids", 10, 10_000.00)
        self.other_robot = Robot("2x21", "Education", 200, 9_000.00)

    def test_initialization_with_correct_data(self):
        self.assertEqual("1x23", self.sample_robot.robot_id)
        self.assertEqual("Humanoids", self.sample_robot.category)
        self.assertEqual(10, self.sample_robot.available_capacity)
        self.assertEqual(10_000.00, self.sample_robot.price)
        self.assertEqual([], self.sample_robot.hardware_upgrades)
        self.assertEqual([], self.sample_robot.software_updates)

    def test_initialization_with_invalid_category_robot_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sample_robot.category = "invalid category"
        expected_msg = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected_msg, str(ex.exception))

    def test_initialization_with_negative_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.sample_robot.price = - 1
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_successful_upgrade(self):
        return_msg = self.sample_robot.upgrade("new hardware", 1_200)
        self.assertEqual(["new hardware"], self.sample_robot.hardware_upgrades)
        self.assertEqual(11_800.00, self.sample_robot.price)
        self.assertEqual("Robot 1x23 was upgraded with new hardware.", return_msg)

    def test_unsuccessful_upgrade_with_already_installed_hardware(self):
        self.sample_robot.hardware_upgrades.append("new hardware")
        return_msg = self.sample_robot.upgrade("new hardware", 1_200)
        self.assertEqual("Robot 1x23 was not upgraded.", return_msg)

    def test_successful_update(self):
        return_msg = self.sample_robot.update(1.215, 5)
        self.assertEqual([1.215], self.sample_robot.software_updates)
        self.assertEqual(5, self.sample_robot.available_capacity)
        self.assertEqual("Robot 1x23 was updated to version 1.215.", return_msg)

    def test_unsuccessful_update_with_already_latest_version_installed(self):
        self.sample_robot.software_updates.append(1.215)
        return_msg = self.sample_robot.update(1.123, 5)
        self.assertEqual("Robot 1x23 was not updated.", return_msg)

    def test_unsuccessful_update_due_to_insufficient_capacity(self):
        return_msg = self.sample_robot.update(1.123, 20)
        self.assertEqual("Robot 1x23 was not updated.", return_msg)

    def test_greater_than_with_greater_than(self):
        return_msg = self.sample_robot.__gt__(self.other_robot)
        expected_msg = f"Robot with ID 1x23 is more expensive than Robot with ID 2x21."
        self.assertEqual(expected_msg, return_msg)

    def test_greater_than_with_equality(self):
        self.other_robot.price = 10_000.00
        return_msg = self.sample_robot.__gt__(self.other_robot)
        expected_msg = f"Robot with ID 1x23 costs equal to Robot with ID 2x21."
        self.assertEqual(expected_msg, return_msg)

    def test_greater_than_with_less_than(self):
        return_msg = self.other_robot.__gt__(self.sample_robot)
        expected_msg = f"Robot with ID 2x21 is cheaper than Robot with ID 1x23."
        self.assertEqual(expected_msg, return_msg)


if __name__ == '__main__':
    main()
