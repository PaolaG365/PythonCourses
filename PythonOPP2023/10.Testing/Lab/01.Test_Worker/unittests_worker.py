from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker1 = Worker("Peter", 15000, 100)

    def test_worker_initialization(self):
        self.assertEqual("Peter", self.worker1.name)
        self.assertEqual(15000, self.worker1.salary)
        self.assertEqual(100, self.worker1.energy)
        self.assertEqual(0, self.worker1.money)

    def test_work_method_with_enough_energy(self):
        self.worker1.work()

        self.assertEqual(15000, self.worker1.money)
        self.assertEqual(99, self.worker1.energy)

    def test_work_method_with_not_enough_energy_raises_ex(self):
        self.worker1.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker1.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_method(self):
        self.worker1.rest()
        self.assertEqual(101, self.worker1.energy)

    def test_get_info_method(self):
        self.worker1.money = self.worker1.salary
        self.assertEqual("Peter has saved 15000 money.", self.worker1.get_info())


if __name__ == "__main__":
    main()
