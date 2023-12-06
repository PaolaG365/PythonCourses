from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):

    def __init__(self):
        super().__init__(protection=120, price=15.0)

    @property
    def eq_type(self):
        return "KneePad"

    def increase_price(self):
        self.price += self.price * 0.2
