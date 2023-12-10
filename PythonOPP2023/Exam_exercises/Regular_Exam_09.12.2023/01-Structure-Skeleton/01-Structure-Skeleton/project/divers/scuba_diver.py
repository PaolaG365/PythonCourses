from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    @property
    def diver_type(self):
        return "ScubaDiver"

    def miss(self, time_to_catch: int):
        new_level = int(self.oxygen_level - time_to_catch * 0.3)
        if new_level > 0:
            self.oxygen_level = new_level
        else:
            self.oxygen_level = new_level
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
