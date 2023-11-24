from calendar import month_name


class DVD:
    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        month, year = [int(x) for x in date.split(".")[1:]]
        released_month = month_name[month]
        return cls(name, _id, year, released_month, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction"
                f" {self.age_restriction}. Status:{' not ' if not self.is_rented else ' '}rented")
