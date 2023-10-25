moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

player_row, player_col = 0, 0
field_matrix = []
rows, cols = [int(x) for x in input().split()]
TARGET_COUNT = 3
touched_count, counter_moves = 0, 0


def valid_indices(row, col):
    return 0 <= row < rows and 0 <= col < cols


for row_field in range(rows):
    field_matrix.append([])
    col_index = 0
    for el in input().split():
        if el == "B":
            player_row, player_col = row_field, col_index
        col_index += 1
        field_matrix[row_field].append(el)

command = input()
while command != "Finish":
    next_row = player_row + moves[command][0]
    next_col = player_col + moves[command][1]
    if not valid_indices(next_row, next_col):
        pass
    elif field_matrix[next_row][next_col] == "O":
        pass
    else:
        if field_matrix[next_row][next_col] == "P":
            touched_count += 1
            if touched_count == TARGET_COUNT:
                field_matrix[next_row][next_col] = "-"
                counter_moves += 1
                break
        field_matrix[next_row][next_col] = "-"
        counter_moves += 1
        player_row, player_col = next_row, next_col

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_count} Moves made: {counter_moves}")
