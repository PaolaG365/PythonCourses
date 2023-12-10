from project.booths.booth import Booth


class OpenBooth(Booth):
    RESERVATION_PRICE_PER_CUSTOMER = 2.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self.RESERVATION_PRICE_PER_CUSTOMER * number_of_people
        self.is_reserved = True
