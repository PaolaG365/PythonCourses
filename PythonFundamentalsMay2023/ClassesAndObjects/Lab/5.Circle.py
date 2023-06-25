class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return self.diameter * Circle.__pi

    def calculate_area(self):
        return (self.radius ** 2) * Circle.__pi

    def calculate_area_of_sector(self, angle):
        return (angle/360) * (self.radius ** 2) * Circle.__pi


circle = Circle(10)
angle_circle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle_circle):.2f}")