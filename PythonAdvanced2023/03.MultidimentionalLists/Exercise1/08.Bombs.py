def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


def bomb_explosion(row_bomb, col_bomb, bomb_dmg, matrix):
    for row in range(row_bomb - 1, row_bomb + 2):
        for col in range(col_bomb - 1, col_bomb + 2):
            if are_valid_indices(row, col, matrix) and matrix[row][col] > 0:
                matrix[row][col] -= bomb_dmg
    return matrix


rows = int(input())
sample_matrix = [[int(x) for x in input().split()] for _ in range(rows)]
coordinates_bombs = input().split()


for coord in range(len(coordinates_bombs)):
    bomb_row, bomb_col = [int(x) for x in coordinates_bombs[coord].split(",")]
    if sample_matrix[bomb_row][bomb_col] <= 0:
        continue
    bomb_value = sample_matrix[bomb_row][bomb_col]
    sample_matrix[bomb_row][bomb_col] = 0
    sample_matrix = bomb_explosion(bomb_row, bomb_col, bomb_value, sample_matrix)

# alive_cells = [el for matrix_row in sample_matrix for el in matrix_row if el > 0]
alive_cells = []
for matrix_row in sample_matrix:
    alive_cells.extend(row_el for row_el in matrix_row if row_el > 0)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*m_row) for m_row in sample_matrix]
