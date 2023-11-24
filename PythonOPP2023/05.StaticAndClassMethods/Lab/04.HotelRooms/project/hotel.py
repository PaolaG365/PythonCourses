from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, guests_n: int):
        room_existing = next((n_room for n_room in self.rooms if n_room.number == room_number), None)
        if room_existing:
            room_existing.take_room(guests_n)

    def free_room(self, room_number: int):
        room_existing = next((n_room for n_room in self.rooms if n_room.number == room_number), None)
        if room_existing:
            room_existing.free_room()

    def status(self):
        return (f"Hotel {self.name} has {sum(x.guests for x in self.rooms)} total guests\n"
                f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}"
                f"\nTaken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}")
