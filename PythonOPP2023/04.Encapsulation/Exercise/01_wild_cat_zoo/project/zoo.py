from typing import List, Dict
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        employees_salary = sum(worker.salary for worker in self.workers)
        if self.__budget < employees_salary:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= employees_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_monthly = sum(animal.money_for_care for animal in self.animals)
        if self.__budget < animals_monthly:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_monthly
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    # right way to get 100/100
    # @staticmethod
    # def __print_status(list_data: List[object], *target_sets):
    #     data_sets: Dict[str: List[str]] = {set_target: [] for set_target in target_sets}
    #
    #     for data in list_data:
    #         data_sets[data.__class__.__name__].append(repr(data))
    #
    #     final_data = [f"You have {len(list_data)} {str(list_data[0].__class__.__bases__[0].__name__).lower()}s"]
    #
    #     for obj_name, obj_info in data_sets.items():
    #         final_data.append(f"----- {len(obj_info)} {obj_name}s:")
    #         final_data.extend(obj_info)
    #
    #     return "\n".join(final_data)
    #
    # def animals_status(self):
    #     return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")
    #
    # def workers_status(self):
    #     return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    # like this a little better, wouldn't get full score since it's not the way
    # to be solved, output needs to be an exact way
    def animals_status(self):
        return self.__print_status(self.animals)  # , [str(n).split(".")[-1].strip("'>") for n in self.animals])

    def workers_status(self):
        return self.__print_status(self.workers)  # , [str(n).split(".")[-1].strip("'>") for n in self.workers])

    @staticmethod
    def __print_status(objects_data):
        data: Dict[str: List[str]] = {}
        for obj in objects_data:
            data.setdefault(obj.__class__.__name__, [])
            data[obj.__class__.__name__].append(repr(obj))

        final_data = [f"You have {len(objects_data)} {str(objects_data[0].__class__.__bases__[0].__name__).lower()}s"]

        for obj_class, objs_repr in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
            final_data.append(f"----- {len(objs_repr)} {obj_class}s:")
            final_data.extend(objs_repr)

        return '\n'.join(final_data)
