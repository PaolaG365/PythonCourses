from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTERS = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTERS:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.VALID_COMPUTERS[type_computer](manufacturer, model)
        config_res = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return config_res

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        clients_dreams = next((comp_obj for comp_obj in self.warehouse
                               if comp_obj.price <= client_budget and
                               comp_obj.processor == wanted_processor and
                               comp_obj.ram >= wanted_ram), None)

        if not clients_dreams:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - clients_dreams.price
        self.warehouse.remove(clients_dreams)
        return f"{clients_dreams.__repr__()} sold for {client_budget}$."
