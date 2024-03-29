from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_numbers_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        numeric_value = 0

        for i in range(len(value)):
            if value[i] in roman_numbers_value:
                if i + 1 < len(value) and roman_numbers_value[value[i]] < roman_numbers_value[value[i + 1]]:
                    numeric_value -= roman_numbers_value[value[i]]
                else:
                    numeric_value += roman_numbers_value[value[i]]

        return cls(numeric_value)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str) or not value.isdigit():
            return "wrong type"
        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
