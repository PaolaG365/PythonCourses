import re

numbers_string = input()

valid_nums_pattern = re.compile(r"(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?($|(?=\s))")

valid_numbers = re.finditer(valid_nums_pattern, numbers_string)

for number in valid_numbers:
    print(number.group(), end=" ")
