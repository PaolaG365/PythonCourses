from typing import List, Type

from project.animals.animal import Bird
from project.food import Meat, Seed, Vegetable, Fruit


class Owl(Bird):
    @property
    def diet(self) -> List[Type]:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def diet(self) -> List[Type]:
        return [Meat, Seed, Fruit, Vegetable]

    @property
    def weight_gain(self) -> float:
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
