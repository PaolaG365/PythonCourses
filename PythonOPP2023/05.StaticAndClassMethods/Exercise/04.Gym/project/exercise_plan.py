class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration_in_min: int):
        self.id = ExercisePlan.id
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration_in_min
        ExercisePlan.id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, duration_in_hours: int):
        to_min = duration_in_hours * 60
        return cls(trainer_id, equipment_id, to_min)

    @staticmethod
    def get_next_id():
        return ExercisePlan.id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
