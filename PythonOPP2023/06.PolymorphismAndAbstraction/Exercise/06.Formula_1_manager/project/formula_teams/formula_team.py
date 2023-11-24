from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):  # -> Dict[str: Dict[int: int]],  {sponsor: {rank: money}}
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for sponsorship in self.sponsors.values():
            for rank_sponsorship in sponsorship:
                if race_pos <= rank_sponsorship:
                    revenue += sponsorship[rank_sponsorship]
                    break

        revenue -= self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
