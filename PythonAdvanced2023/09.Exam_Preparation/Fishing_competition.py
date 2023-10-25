moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
TARGET_CATCH_TONS = 20
current_catch = 0
ship_row, ship_col = 0, 0
sea_matrix = []
square_rows = int(input())


def index_handling(row, col):
    row = square_rows - 1 if 0 > row else row
    row = 0 if row >= square_rows else row
    col = square_rows - 1 if 0 > col else col
    col = 0 if col >= square_rows else col
    return row, col


for row_sea in range(square_rows):
    sea_matrix.append([])
    col_sea = 0
    for el in input():
        if el == "S":
            ship_row, ship_col = row_sea, col_sea
        col_sea += 1
        sea_matrix[row_sea].append(el)

command = input()
while command != "collect the nets":
    next_row, next_col = index_handling(ship_row + moves[command][0], ship_col + moves[command][1])
    next_step = sea_matrix[next_row][next_col]

    if next_step.isdigit():
        current_catch += int(next_step)
    if next_step == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{next_row},{next_col}]")
        exit()
    sea_matrix[ship_row][ship_col] = "-"
    sea_matrix[next_row][next_col] = "S"
    ship_row, ship_col = next_row, next_col

    command = input()

if current_catch >= TARGET_CATCH_TONS:
    print("Success! You managed to reach the quota!")
else:
    print("You didn't catch enough fish and didn't reach the quota!", end=" ")
    print(f"You need {TARGET_CATCH_TONS - current_catch} tons of fish more.")
if current_catch:
    print(f"Amount of fish caught: {current_catch} tons.")

[print(*sea_wave, sep="") for sea_wave in sea_matrix]
