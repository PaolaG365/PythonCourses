from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST)

    @property
    def client_type(self):
        return 'Adult'

    def increase_clients_interest(self):
        self.interest += 2.0