from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat1 = Cat("Tabby")

    def test_feeding_cat_when_hungry(self):
        self.cat1.eat()
        self.assertTrue(self.cat1.fed)
        self.assertTrue(self.cat1.sleepy)
        self.assertEqual(1, self.cat1.size)

    def test_feeding_cat_when_already_fed(self):
        self.cat1.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat1.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_putting_the_cat_to_sleep(self):
        self.cat1.sleepy = True
        self.cat1.fed = True
        self.cat1.sleep()
        self.assertFalse(self.cat1.sleepy)

    def test_putting_the_cat_to_sleep_while_hungry(self):
        self.cat1.sleepy = True
        with self.assertRaises(Exception) as ex:
            self.cat1.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == '__main__':
    main()
