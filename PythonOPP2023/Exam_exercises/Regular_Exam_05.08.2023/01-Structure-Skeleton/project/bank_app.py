from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next(loan_obj for loan_obj in self.loans if loan_obj.loan_type == loan_type)
        client = next(client_obj for client_obj in self.clients if client_obj.client_id == client_id)

        if loan.loan_meant_for != client.client_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        client = next((client_obj for client_obj in self.clients if client_obj.client_id == client_id), None)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = [loan.increase_interest_rate() for loan in self.loans
                         if loan.loan_type == loan_type]
        return f"Successfully changed {len(changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients_loans = [client.increase_clients_interest() for client in self.clients
                                 if client.interest < min_rate]
        return f"Number of clients affected: {len(changed_clients_loans)}."

    def get_statistics(self):
        clients_loans = self.__get_clients_loans()
        total_sum_granted = sum(loan.amount for loan in clients_loans)
        not_granted_total_sum = sum([loan.amount for loan in self.loans])
        average_interest = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0
        total_clients_income = sum(client.income for client in self.clients)

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_clients_income:.2f}
Granted Loans: {len(clients_loans)}, Total Sum: {total_sum_granted:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_total_sum:.2f}
Average Client Interest Rate: {average_interest:.2f}"""

    def __get_clients_loans(self):
        result = []
        for client in self.clients:
            result.extend(client.loans)
        return result
