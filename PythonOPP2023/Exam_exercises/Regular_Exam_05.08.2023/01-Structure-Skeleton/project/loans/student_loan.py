from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE = 1.5
    AMOUNT = 2000.0

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    @property
    def loan_type(self):
        return "StudentLoan"

    @property
    def loan_meant_for(self):
        return "Student"

    def increase_interest_rate(self):
        self.interest_rate += 0.2
