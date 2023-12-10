from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.TIME_TO_CATCH)

    @property
    def fish_type(self):
        return "PredatoryFish"

    def fish_details(self):
        return (f"{self.fish_type}: {self.name} [Points: {self.points}, "
                f"Time to Catch: {self.time_to_catch} seconds]")
