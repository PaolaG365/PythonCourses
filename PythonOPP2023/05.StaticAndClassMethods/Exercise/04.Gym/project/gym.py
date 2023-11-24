from typing import List, Any, Generator
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def __add_object_to_list(obj_list, obj):
        if obj not in obj_list:
            obj_list.append(obj)

    def add_customer(self, customer: Customer):
        self.__add_object_to_list(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.__add_object_to_list(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.__add_object_to_list(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_object_to_list(self.plans, plan)

    def add_subscription(self, sub: Subscription):
        self.__add_object_to_list(self.subscriptions, sub)

    def subscription_info(self, subscription_id: int):
        subscription = next((sub for sub in self.subscriptions if sub.id == subscription_id), None)
        exercise = next((exercise_plan for exercise_plan in self.plans if exercise_plan.id == subscription.exercise_id))
        result = [repr(subscription)]
        result.extend(repr(customer) for customer in self.customers if customer.id == subscription.customer_id)
        result.extend(repr(trainer) for trainer in self.trainers if trainer.id == subscription.trainer_id)
        result.extend(repr(tool) for tool in self.equipment if tool.id == exercise.equipment_id)
        result.append(repr(exercise))
        return "\n".join(result)
