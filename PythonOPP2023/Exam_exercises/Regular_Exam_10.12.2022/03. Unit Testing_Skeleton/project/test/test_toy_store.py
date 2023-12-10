from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_initialization(self):
        for letter_shelf in range(ord("A"), ord("G") + 1):
            self.assertEqual(None, self.toy_store.toy_shelf[chr(letter_shelf)])

    def test_add_toy_on_non_existent_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("L", "teddy bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_toy_already_on_shelf(self):
        self.toy_store.add_toy("A", "teddy bear")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "teddy bear")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_with_different_toy_on_shelf(self):
        self.toy_store.add_toy("A", "dolly")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "teddy bear")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_on_free_existing_shelf(self):
        return_msg = self.toy_store.add_toy("A", "teddy bear")
        self.assertEqual("Toy:teddy bear placed successfully!", return_msg)
        self.assertEqual({
            "A": "teddy bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_remove_toy_from_non_existing_shelf_raises_exc(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("L", "doll")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_from_wrong_shelf_raises_exc(self):
        self.toy_store.add_toy("A", "teddy bear")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "doll")
        self.assertEqual("Toy in that shelf doesn't exists!", str( ex.exception))

    def test_remove_toy_from_shelf_with_existing_toy(self):
        self.toy_store.add_toy("A", "teddy bear")
        return_msg = self.toy_store.remove_toy("A", "teddy bear")
        self.assertEqual("Remove toy:teddy bear successfully!", return_msg)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)


if __name__ == '__main__':
    main()
