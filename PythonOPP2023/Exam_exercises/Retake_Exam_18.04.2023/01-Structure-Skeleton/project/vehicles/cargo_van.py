from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    ADDITIONAL_ENERGY_CONSUMED = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        battery_used_in_percentages = round((mileage / self.max_mileage) * 100) + self.ADDITIONAL_ENERGY_CONSUMED
        self.battery_level -= battery_used_in_percentages
