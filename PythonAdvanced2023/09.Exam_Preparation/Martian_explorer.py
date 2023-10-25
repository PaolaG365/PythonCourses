moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
type_deposits = {"W": "Water", "M": "Metal", "C": "Concrete"}
found_deposits = {resource: 0 for resource in type_deposits.values()}
MARS_ROWS, MARS_COLS = 6, 6
mars_matrix = []
rover_row, rover_col = 0, 0


def index_handling(row, col):
    row = MARS_ROWS - 1 if 0 > row else row
    row = 0 if row >= MARS_ROWS else row
    col = MARS_COLS - 1 if 0 > col else col
    col = 0 if col >= MARS_COLS else col
    return row, col


for row_mars in range(MARS_ROWS):
    col_index = 0
    mars_matrix.append([])
    for el in input().split():
        if el == "E":
            rover_row, rover_col = row_mars, col_index
        col_index += 1
        mars_matrix[row_mars].append(el)

commands = input().split(", ")

for command in commands:
    next_row, next_col = index_handling(rover_row + moves[command][0], rover_col + moves[command][1])
    next_step = mars_matrix[next_row][next_col]

    if next_step in type_deposits:
        print(f"{type_deposits[next_step]} deposit found at ({next_row}, {next_col})")
        found_deposits[type_deposits[next_step]] += 1

    elif next_step == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    rover_row, rover_col = next_row, next_col

if all(found_deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
