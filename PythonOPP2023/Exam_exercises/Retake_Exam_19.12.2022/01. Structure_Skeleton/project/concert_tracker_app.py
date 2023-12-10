from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    NEEDED_SKILLS_FOR_MUSICIANS_BY_GENRE = {
        "Rock": {"Drummer": ["play the drums with drumsticks"],
                 "Singer": ["sing high pitch notes"],
                 "Guitarist": ["play rock"]},

        "Metal": {"Drummer": ["play the drums with drumsticks"],
                  "Singer": ["sing low pitch notes"],
                  "Guitarist": ["play metal"]},

        "Jazz": {"Drummer": ["play the drums with drum brushes"],
                 "Singer": ["sing high pitch notes", "sing low pitch notes"],
                 "Guitarist": ["play jazz"]},
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        existing_musician = next((musician for musician in self.musicians if musician.name == name), None)
        if existing_musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        existing_band = next((band for band in self.bands if band.name == name), None)
        if existing_band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        existing_concert = next((concert for concert in self.concerts if concert.place == place), None)
        if existing_concert:
            raise Exception(f"{existing_concert.place} is already registered for {existing_concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((musician for musician in self.musicians if musician.name == musician_name), None)
        band = next((band for band in self.bands if band.name == band_name), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((band for band in self.bands if band.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next((musician for musician in band.members if musician.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next((band for band in self.bands if band.name == band_name), None)
        concert = next((concert for concert in self.concerts if concert.place == concert_place), None)

        singers = [member for member in band.members if member.musician_type == "Singer"]
        guitarists = [member for member in band.members if member.musician_type == "Guitarist"]
        drummers = [member for member in band.members if member.musician_type == "Drummer"]

        if not all([len(singers), len(guitarists), len(drummers)]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        green_light_concert = self.__check_needed_skills_for_musicians(concert.genre, [*singers, *guitarists, *drummers])
        if not green_light_concert:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def __check_needed_skills_for_musicians(self, genre: str, band_members_list: list) -> bool:
        skills = self.NEEDED_SKILLS_FOR_MUSICIANS_BY_GENRE[genre]

        for type_musician, musician_skills in skills.items():
            members_to_check = [member for member in band_members_list if member.musician_type == type_musician]
            for skill in musician_skills:
                checked_members = [member for member in members_to_check if skill in member.skills]
                if len(checked_members) != len(members_to_check):
                    return False
        return True
