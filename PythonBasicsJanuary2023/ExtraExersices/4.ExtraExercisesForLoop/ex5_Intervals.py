moves_in_game = int(input())

result = 0
first_range, second_range, third_range, fourth_range, fifth_range, invalid = 0, 0, 0, 0, 0, 0

for _ in range(moves_in_game):
    number = int(input())
    if 0 > number or number > 50:
        result /= 2
        invalid += 1
    elif number < 10:
        result += number * 0.2
        first_range += 1
    elif number < 20:
        result += number * 0.3
        second_range += 1
    elif number < 30:
        result += number * 0.4
        third_range += 1
    elif number < 40:
        result += 50
        fourth_range += 1
    elif number <= 50:
        result += 100
        fifth_range += 1

print(f'{result:.2f}')
print(f"From 0 to 9: {first_range / moves_in_game * 100:.2f}%")
print(f"From 10 to 19: {second_range / moves_in_game * 100:.2f}%")
print(f"From 20 to 29: {third_range / moves_in_game * 100:.2f}%")
print(f"From 30 to 39: {fourth_range / moves_in_game * 100:.2f}%")
print(f"From 40 to 50: {fifth_range / moves_in_game * 100:.2f}%")
print(f"Invalid numbers: {invalid / moves_in_game * 100:.2f}%")
