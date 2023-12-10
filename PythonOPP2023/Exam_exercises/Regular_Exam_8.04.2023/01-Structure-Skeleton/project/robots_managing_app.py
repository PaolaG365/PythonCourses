from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        hiring_service = next(service for service in self.services if service.name == service_name)
        applying_robot = next(robot for robot in self.robots if robot.name == robot_name)

        if hiring_service.service_type != applying_robot.service_type_provided:
            return "Unsuitable service."

        if len(hiring_service.robots) >= hiring_service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(applying_robot)
        hiring_service.robots.append(applying_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(service for service in self.services if service.name == service_name)
        quitting_robot = next((robot for robot in service.robots if robot.name == robot_name), None)

        if not quitting_robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(quitting_robot)
        self.robots.append(quitting_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(service for service in self.services if service.name == service_name)
        fed_robots = [robot.eating() for robot in service.robots]
        return f"Robots fed: {len(fed_robots)}."

    def service_price(self, service_name: str):
        service = next(service for service in self.services if service.name == service_name)
        total_price = sum([robot.price for robot in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([service.details() for service in self.services])
