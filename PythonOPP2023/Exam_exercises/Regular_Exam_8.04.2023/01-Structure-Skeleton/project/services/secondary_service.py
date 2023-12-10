from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    @property
    def service_type(self):
        return "SecondaryService"

    def details(self):
        return (f"{self.name} Secondary Service:\nRobots: "
                f"{' '.join([robot.name for robot in self.robots]) if self.robots else 'none'}")
