from project.animal import Animal


class Camel(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 30)
