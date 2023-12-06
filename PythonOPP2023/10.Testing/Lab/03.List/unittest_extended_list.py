from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.sample_list = IntegerList(1, 2, 3, 4, 5, 5.5, "string")

    def test_initialization(self):
        self.assertNotIn(5.5, self.sample_list._IntegerList__data)
        self.assertNotIn("string", self.sample_list._IntegerList__data)

    def test_get_data_method_returns_list(self):
        int_list = self.sample_list.get_data()
        self.assertIsInstance(int_list, list)
        self.assertTrue(all(isinstance(el, int) for el in int_list))

    def test_add_method_with_valid_data(self):
        ints_list = self.sample_list.add(7)
        self.assertIn(7, ints_list)

    def test_add_method_with_invalid_data_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.sample_list.add("string")

        self.assertEqual("Element is not Integer", str(err.exception))

    def test_remove_method_with_valid_index(self):
        removed_num = self.sample_list.remove_index(0)
        self.assertNotIn(removed_num, self.sample_list.get_data())

    def test_remove_method_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as err:
            self.sample_list.remove_index(len(self.sample_list.get_data()))
        self.assertEqual("Index is out of range", str(err.exception))

    def test_get_method_with_valid_index(self):
        num = self.sample_list.get_data()[2]
        self.assertEqual(num, self.sample_list.get(2))

    def test_get_method_with_invalid_dat_raises_index_error(self):
        with self.assertRaises(IndexError) as err:
            self.sample_list.get(10)
        self.assertEqual("Index is out of range", str(err.exception))

    def test_insert_method_with_valid_index(self):
        new_list = [16, 1, 2, 3, 4, 5]
        self.sample_list.insert(0, 16)
        self.assertEqual(new_list, self.sample_list.get_data())

    def test_insert_method_with_invalid_index(self):
        with self.assertRaises(IndexError) as err:
            self.sample_list.insert(20, 100)
        self.assertEqual("Index is out of range", str(err.exception))

    def test_insert_method_with_non_integer_value(self):
        with self.assertRaises(ValueError) as err:
            self.sample_list.insert(0, "string")
        self.assertEqual("Element is not Integer", str(err.exception))

    def test_get_biggest_value_method_works(self):
        max_value = max(self.sample_list.get_data())
        self.assertEqual(max_value, self.sample_list.get_biggest())

    def test_get_index_method_works(self):
        self.assertEqual(0, self.sample_list.get_index(1))


if __name__ == "__main__":
    main()
