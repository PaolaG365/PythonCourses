from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        existing_user = next((user for user in self.users if user.driving_license_number == driving_license_number), None)

        if existing_user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if next((vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number), None):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        existing_route_equal_length = next((route for route in self.routes
                                            if route.start_point == start_point
                                            and route.end_point == end_point
                                            and route.length == length), None)

        existing_route_less_length = next((route for route in self.routes
                                           if route.start_point == start_point
                                           and route.end_point == end_point
                                           and route.length < length), None)

        existing_route_bigger_length = next((route for route in self.routes
                                             if route.start_point == start_point
                                             and route.end_point == end_point
                                             and route.length > length), None)

        if existing_route_equal_length:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if existing_route_less_length:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        if existing_route_bigger_length:
            existing_route_bigger_length.is_locked = True

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user_traveling = next(user for user in self.users if user.driving_license_number == driving_license_number)
        vehicle_for_trip = next(vehicle for vehicle in self.vehicles
                                if vehicle.license_plate_number == license_plate_number)
        route_to_travel = next(route for route in self.routes if route.route_id == route_id)

        if user_traveling.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle_for_trip.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route_to_travel.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle_for_trip.drive(route_to_travel.length)

        if is_accident_happened:
            vehicle_for_trip.change_status()
            user_traveling.decrease_rating()
        else:
            user_traveling.increase_rating()

        return vehicle_for_trip.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))[:count]

        for vehicle in sorted_damaged_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(sorted_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        [result.append(user.__str__()) for user in sorted(self.users, key=lambda x: -x.rating)]

        return "\n".join(result)
