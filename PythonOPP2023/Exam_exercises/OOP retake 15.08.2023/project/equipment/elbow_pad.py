from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25.0)

    @property
    def eq_type(self):
        return "ElbowPad"

    def increase_price(self):
        self.price += self.price * 0.1
