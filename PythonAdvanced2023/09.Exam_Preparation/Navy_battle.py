moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

MAX_HITS_SUSTAINABLE = 2
TARGET_DESTROYED_CRUISERS = 3
hits, destroyed_cruisers = 0, 0
submarine_row, submarine_col = 0, 0
sea_field = []
rows = int(input())

for row_sea in range(rows):
    sea_field.append([])
    col_sea = 0
    for el in input():
        if el == "S":
            submarine_row, submarine_col = row_sea, col_sea
            el = "-"
        col_sea += 1
        sea_field[row_sea].append(el)

while True:
    command = input()
    next_row = submarine_row + moves[command][0]
    next_col = submarine_col + moves[command][1]
    sea_encounter = sea_field[next_row][next_col]

    if sea_encounter == "*":
        hits += 1
        if hits > MAX_HITS_SUSTAINABLE:
            print(
                f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!"
            )
            sea_field[submarine_row][submarine_col] = "-"
            sea_field[next_row][next_col] = "S"
            break

    if sea_encounter == "C":
        destroyed_cruisers += 1
        if destroyed_cruisers == TARGET_DESTROYED_CRUISERS:
            print(
                "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
            )
            sea_field[submarine_row][submarine_col] = "-"
            sea_field[next_row][next_col] = "S"
            break

    sea_field[submarine_row][submarine_col] = "-"
    sea_field[next_row][next_col] = "S"
    submarine_row, submarine_col = next_row, next_col

[print(*wave, sep="") for wave in sea_field]
