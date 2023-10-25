moves = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}

mouse_position = []
cheese_counter = 0
rows_cupboard, cols_cupboard = [int(x) for x in input().split(",")]
cupboard_matrix = []


# just so cols input is used at least once
def are_valid_indices(row, col): return 0 <= row < rows_cupboard and 0 <= col < cols_cupboard


for row_matrix in range(rows_cupboard):
    cupboard_matrix.append([])
    col_counter = 0

    for el in input():
        if el == "M":
            mouse_position = [row_matrix, col_counter]
        elif el == "C":
            cheese_counter += 1
        col_counter += 1
        cupboard_matrix[row_matrix].append(el)

command = input()
while command != "danger":
    next_row = mouse_position[0] + moves[command][0]
    next_col = mouse_position[1] + moves[command][1]

    if not are_valid_indices(next_row, next_col):
        print("No more cheese for tonight!")
        break

    elif cupboard_matrix[next_row][next_col] == "@":
        pass

    else:
        next_step = cupboard_matrix[next_row][next_col]
        cupboard_matrix[mouse_position[0]][mouse_position[1]] = "*"
        mouse_position = [next_row, next_col]
        cupboard_matrix[next_row][next_col] = "M"

        if next_step == "C":
            cheese_counter -= 1

            if cheese_counter == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        elif next_step == "T":
            print("Mouse is trapped!")
            break

    command = input()

else:
    if cheese_counter > 0:
        print("Mouse will come back later!")

[print("".join(cupboard_row)) for cupboard_row in cupboard_matrix]
