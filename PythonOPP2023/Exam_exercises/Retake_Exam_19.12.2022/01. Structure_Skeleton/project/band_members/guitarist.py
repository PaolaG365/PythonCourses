from project.band_members.musician import Musician


class Guitarist(Musician):
    AVAILABLE_SKILLS = [
        "play metal",
        "play rock",
        "play jazz"
    ]

    @property
    def musician_type(self):
        return "Guitarist"
