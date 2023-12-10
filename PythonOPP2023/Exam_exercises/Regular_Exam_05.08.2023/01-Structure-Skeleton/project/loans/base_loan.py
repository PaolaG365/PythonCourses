from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @property
    @abstractmethod
    def loan_type(self):
        pass

    @property
    @abstractmethod
    def loan_meant_for(self):
        pass

    @abstractmethod
    def increase_interest_rate(self):
        pass
