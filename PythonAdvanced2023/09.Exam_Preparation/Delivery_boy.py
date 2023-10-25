moves = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
row_start, col_start = 0, 0
d_boy_row, d_boy_col = 0, 0
field_matrix = []
rows, cols = [int(x) for x in input().split()]


def are_valid_indices(row, col): return 0 <= row < rows and 0 <= col < cols


for row_field in range(rows):
    field_matrix.append([])
    col_counter = 0
    for el in input():
        if el == "B":
            d_boy_row, d_boy_col = row_field, col_counter
            row_start, col_start = row_field, col_counter
        col_counter += 1
        field_matrix[row_field].append(el)

while True:
    command = input()
    next_row = d_boy_row + moves[command][0]
    next_col = d_boy_col + moves[command][1]

    if are_valid_indices(next_row, next_col):
        next_box = field_matrix[next_row][next_col]
        if next_box == "*":
            continue

        if next_box == "P":
            field_matrix[next_row][next_col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        if next_box == "A":
            field_matrix[next_row][next_col] = "P"
            print("Pizza is delivered on time! Next order...")
            break
        if field_matrix[next_row][next_col] != "R" and field_matrix[next_row][next_col] != "B":
            field_matrix[next_row][next_col] = "."
        d_boy_row, d_boy_col = next_row, next_col

    else:
        field_matrix[row_start][col_start] = " "
        print("The delivery is late. Order is canceled.")
        break

[print(*row, sep="") for row in field_matrix]
