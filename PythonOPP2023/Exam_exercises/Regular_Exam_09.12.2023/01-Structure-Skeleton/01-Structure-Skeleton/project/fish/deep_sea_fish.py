from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.TIME_TO_CATCH)

    @property
    def fish_type(self):
        return "DeepSeaFish"

    def fish_details(self):
        return (f"{self.fish_type}: {self.name} [Points: {self.points}, "
                f"Time to Catch: {self.time_to_catch} seconds]")
