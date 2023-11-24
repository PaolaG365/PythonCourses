class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, guests_n: int):
        if self.is_taken or self.capacity < guests_n:
            return f"Room number {self.number} cannot be taken"
        self.guests = guests_n
        self.is_taken = True

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.guests = 0
        self.is_taken = False
