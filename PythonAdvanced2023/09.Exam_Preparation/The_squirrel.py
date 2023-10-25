squirrel_row, squirrel_col = 0, 0
HAZELNUTS_TARGET = 3
collected_hazelnuts = 0
forest_matrix = []

moves = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}


def valid_indices(row, col, matrix): return 0 <= row < rows_forest and 0 <= col < len(matrix[row])


rows_forest = int(input())
commands = input().split(", ")

for row_forest in range(rows_forest):
    forest_matrix.append([])
    col_forest = 0
    for el in input():
        if el == "s":
            squirrel_row, squirrel_col = row_forest, col_forest
        col_forest += 1
        forest_matrix[row_forest].append(el)

for command in commands:
    next_row = squirrel_row + moves[command][0]
    next_col = squirrel_col + moves[command][1]

    if valid_indices(next_row, next_col, forest_matrix):
        forest_box = forest_matrix[next_row][next_col]
        forest_matrix[squirrel_row][squirrel_col] = "*"
        squirrel_row, squirrel_col = next_row, next_col
        forest_matrix[next_row][next_col] = "s"

        if forest_box == "h":
            collected_hazelnuts += 1

            if collected_hazelnuts == HAZELNUTS_TARGET:
                print("Good job! You have collected all hazelnuts!")
                break

        elif forest_box == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break

    else:
        print("The squirrel is out of the field.")
        break
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
