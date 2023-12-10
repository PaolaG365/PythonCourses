from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.INITIAL_WEIGHT)

    @property
    def service_type_provided(self):
        return "SecondaryService"

    def eating(self):
        self.weight += 1
