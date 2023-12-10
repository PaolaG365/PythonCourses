from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    @property
    def diver_type(self):
        return "FreeDiver"

    def miss(self, time_to_catch: int):
        new_level = int(self.oxygen_level - time_to_catch * 0.6)
        if new_level > 0:
            self.oxygen_level = new_level
        else:
            self.oxygen_level = 0
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
