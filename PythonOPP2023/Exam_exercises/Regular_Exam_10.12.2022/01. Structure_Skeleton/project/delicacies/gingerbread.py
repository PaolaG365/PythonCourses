from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name=name, portion=self.PORTION, price=price)

    @property
    def delicacy_type(self):
        return "Gingerbread"

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
