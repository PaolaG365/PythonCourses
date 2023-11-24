from typing import List, Type

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    @property
    def diet(self) -> List[Type]:
        return [Vegetable, Fruit]

    @property
    def weight_gain(self) -> float:
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    @property
    def diet(self) -> List[Type]:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def diet(self) -> List[Type]:
        return [Vegetable, Meat]

    @property
    def weight_gain(self) -> float:
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def diet(self) -> List[Type]:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
