from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        created_eq = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(created_eq)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        created_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(created_team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team_buying = next((team for team in self.teams if team.name == team_name), None)
        equipment_to_sell = next((eq for eq in reversed(self.equipment) if eq.eq_type == equipment_type), None)

        if team_buying.budget < equipment_to_sell.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment_to_sell)
        team_buying.equipment.append(equipment_to_sell)
        team_buying.budget -= equipment_to_sell.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_to_remove = next((team for team in self.teams if team.name == team_name), None)

        if not team_to_remove:
            raise Exception("No such team!")

        if team_to_remove.wins > 0:
            raise Exception(f"The team has {team_to_remove.wins} wins! Removal is impossible!")

        self.teams.remove(team_to_remove)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for equipment in self.equipment:
            if equipment.eq_type == equipment_type:
                counter += 1
                equipment.increase_price()

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = next((team for team in self.teams if team.name == team_name1), None)
        second_team = next((team for team in self.teams if team.name == team_name2), None)

        if first_team.team_type != second_team.team_type:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_points = first_team.advantage + sum(eq.price for eq in first_team.equipment)
        second_team_points = second_team.advantage + sum(eq.price for eq in second_team.equipment)

        if first_team_points == second_team_points:
            return "No winner in this game."

        if first_team_points > second_team_points:
            first_team.win()
            return f"The winner is {team_name1}."

        second_team.win()
        return f"The winner is {team_name2}."

    def get_statistics(self):
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]

        for team in sorted(self.teams, key=lambda x: -x.wins):
            result.append(team.get_statistics())

        return "\n".join(result)
