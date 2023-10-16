"""class ValueCannotBeNegative(Exception):

    def __init__(self, sample_number, message='Number must be positive'):
        self.sample_number = sample_number
        self.message = message
        super().__init__(self.message)


for num in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative(number)

"""


# this is the exercise code
class ValueCannotBeNegative(Exception):
    pass


for num in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
