rows, cols = [int(x) for x in input().split()]

sample_matrix = [[int(el) for el in input().split()] for _ in range(rows)]
matrix_maximus = []
max_sum_inner_matrix = float('-inf')

for row in range(rows - 2):
    for coll in range(cols - 2):
        inner_matrix = []
        sum_matrix = 0
        for row1 in range(row, row + 3):
            inner_matrix.append([sample_matrix[row1][coll], sample_matrix[row1][coll + 1],
                                 sample_matrix[row1][coll + 2]])
            sum_matrix += sum([sample_matrix[row1][coll], sample_matrix[row1][coll + 1],
                               sample_matrix[row1][coll + 2]])
        if sum_matrix > max_sum_inner_matrix:
            max_sum_inner_matrix = sum_matrix
            matrix_maximus = inner_matrix.copy()

print(f"Sum = {max_sum_inner_matrix}")
[print(*matrix) for matrix in matrix_maximus]
