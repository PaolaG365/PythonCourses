from project.band_members.musician import Musician


class Drummer(Musician):
    AVAILABLE_SKILLS = [
        "play the drums with drumsticks",
        "play the drums with drum brushes",
        "read sheet music"]

    @property
    def musician_type(self):
        return "Drummer"
