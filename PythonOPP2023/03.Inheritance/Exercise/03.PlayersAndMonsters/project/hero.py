class Hero:
    def __init__(self, name: str, level: int):
        self.username = name
        self.level = level

    def __str__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"
