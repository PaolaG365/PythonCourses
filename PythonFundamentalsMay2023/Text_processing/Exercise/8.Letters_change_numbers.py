strings = input().split()
total_points = 0

for game_level in strings:
    game = game_level.strip()
    first_letter, number, second_letter = game[0], int(game[1:-1]), game[-1]
    points_level = 0

    if first_letter.isupper():
        points_level += number / (ord(first_letter) - 64)
    else:
        points_level += number * (ord(first_letter) - 96)

    if second_letter.isupper():
        points_level -= (ord(second_letter) - 64)
    else:
        points_level += (ord(second_letter) - 96)

    total_points += points_level

print(f"{total_points:.2f}")
