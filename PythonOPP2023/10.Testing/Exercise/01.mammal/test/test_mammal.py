from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.monkey = Mammal("Pesho", "primate", "monkey sounds")

    def test_initialization(self):
        self.assertEqual("Pesho", self.monkey.name)
        self.assertEqual("primate", self.monkey.type)
        self.assertEqual("monkey sounds", self.monkey.sound)
        self.assertEqual("animals", self.monkey._Mammal__kingdom)

    def test_does_it_make_sound(self):
        self.assertEqual("Pesho makes monkey sounds", self.monkey.make_sound())

    def test_if_its_kingdom_is_animals(self):
        self.assertEqual("animals", self.monkey.get_kingdom())

    def test_info_method_returns_valid_info(self):
        self.assertEqual("Pesho is of type primate", self.monkey.info())


if __name__ == '__main__':
    main()
