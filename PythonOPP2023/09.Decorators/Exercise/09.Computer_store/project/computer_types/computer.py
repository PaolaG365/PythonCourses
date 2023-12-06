from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    RAM_PRICE = 100

    def __init__(self, manufacturer: str, model: str):
        self.model = model
        self.manufacturer = manufacturer
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def available_cpus(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def computer_type(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    def __validate_ram(self, ram: int):
        if not log2(ram).is_integer() or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} "
                             f"{self.manufacturer} {self.model}!")
        return True

    def __validate_processor(self, processor: str):
        if processor not in self.available_cpus:
            raise ValueError(f"{processor} is not compatible with {self.computer_type} "
                             f"{self.manufacturer} {self.model}!")
        return True

    def configure_computer(self, processor: str, ram: int):
        if self.__validate_processor(processor) and self.__validate_ram(ram):
            self.processor = processor
            self.ram = ram
            self.price += int(log2(ram)) * self.RAM_PRICE + self.available_cpus[processor]
            return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
