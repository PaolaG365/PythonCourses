from project.band_members.musician import Musician


class Singer(Musician):
    AVAILABLE_SKILLS = ["sing high pitch notes",
                        "sing low pitch notes"]

    @property
    def musician_type(self):
        return "Singer"
