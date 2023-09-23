rows, cols = [int(x) for x in input().split(', ')]

sample_matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
max_sum_inner_matrix = float('-inf')
inner_matrix = [[], []]

for row in range(rows - 1):
    for col in range(cols - 1):
        sum_matrix = sample_matrix[row][col] + sample_matrix[row][col + 1] + \
                sample_matrix[row + 1][col] + sample_matrix[row + 1][col + 1]
        if sum_matrix > max_sum_inner_matrix:
            max_sum_inner_matrix = sum_matrix
            inner_matrix[0] = [sample_matrix[row][col], sample_matrix[row][col + 1]]
            inner_matrix[1] = [sample_matrix[row + 1][col], sample_matrix[row + 1][col + 1]]

print(*inner_matrix[0])
print(*inner_matrix[1])
print(max_sum_inner_matrix)
