class Vehicle:
    def __init__(self, mileage: int, max_speed=None, gadgets=None):
        self.mileage = mileage
        self.max_speed = max_speed or 150
        self.gadgets = gadgets or []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
