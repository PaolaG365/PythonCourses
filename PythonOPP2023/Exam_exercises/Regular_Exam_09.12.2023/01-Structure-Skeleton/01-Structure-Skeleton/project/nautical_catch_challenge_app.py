from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        existing_diver = next((d for d in self.divers if d.name == diver_name), None)
        if existing_diver:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        existing_fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if existing_fish:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        valid_diver = next((d for d in self.divers if d.name == diver_name), None)
        if not valid_diver:
            return f"{diver_name} is not registered for the competition."

        valid_fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not valid_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if valid_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if valid_diver.oxygen_level < valid_fish.time_to_catch:
            valid_diver.miss(valid_fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif valid_diver.oxygen_level == valid_fish.time_to_catch:
            if is_lucky:
                valid_diver.hit(valid_fish)
                return f"{diver_name} hits a {valid_fish.points}pt. {fish_name}."

            valid_diver.miss(valid_fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        valid_diver.hit(valid_fish)
        return f"{diver_name} hits a {valid_fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_with_health_issues = [d for d in self.divers if d.has_health_issue]
        for diver in divers_with_health_issues:
            diver.update_health_status()
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issues)}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        result = [f"**{diver.name} Catch Report**"]
        [result.append(f.fish_details()) for f in diver.catch]
        return "\n".join(result)

    def competition_statistics(self):
        sorted_divers = sorted(self.divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        [result.append(d.__str__()) for d in sorted_divers if not d.has_health_issue]
        return "\n".join(result)
