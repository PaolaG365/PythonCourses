class Player:
    def __init__(self, name: str, health: int, mana: int):
        self.name = name
        self.hp = health
        self.mp = mana
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        info = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        [info.append(f"==={skill_name} - {mana_cost}") for skill_name, mana_cost in self.skills.items()]
        return "\n".join(info)
