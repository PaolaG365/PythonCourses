from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50_000.0

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    @property
    def loan_type(self):
        return "MortgageLoan"

    @property
    def loan_meant_for(self):
        return "Adult"

    def increase_interest_rate(self):
        self.interest_rate += 0.5
