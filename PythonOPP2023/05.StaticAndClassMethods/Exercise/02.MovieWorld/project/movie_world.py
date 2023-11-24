from typing import List
from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():  # idk
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_obj = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        customer_obj = next((cust for cust in self.customers if cust.id == customer_id), None)

        if dvd_obj in customer_obj.rented_dvds:
            return f"{customer_obj.name} has already rented {dvd_obj.name}"
        if dvd_obj.is_rented:
            return "DVD is already rented"
        if customer_obj.age < dvd_obj.age_restriction:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} to rent this movie"

        customer_obj.rented_dvds.append(dvd_obj)
        dvd_obj.is_rented = True
        return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        dvd_obj = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        customer_obj = next((cust for cust in self.customers if cust.id == customer_id), None)

        if dvd_obj in customer_obj.rented_dvds:
            customer_obj.rented_dvds.remove(dvd_obj)
            dvd_obj.is_rented = False
            return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
        return f"{customer_obj.name} does not have that DVD"

    def __repr__(self):
        result = [cust.__repr__() for cust in self.customers]
        result.extend([dvd.__repr__() for dvd in self.dvds])
        return '\n'.join(result)
