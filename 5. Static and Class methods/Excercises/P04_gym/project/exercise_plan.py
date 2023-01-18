class ExercisePlan:
    ID = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        result = ExercisePlan.ID
        ExercisePlan.ID += 1
        return result

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        hours_in_min = hours * 60
        return cls(trainer_id, equipment_id, hours_in_min)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
