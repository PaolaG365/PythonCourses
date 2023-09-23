rows, cols = [int(x) for x in input().split()]

sample_matrix = [[el for el in input().split()] for _ in range(rows)]
counter_same_els = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if sample_matrix[row][col] == sample_matrix[row][col + 1] == \
           sample_matrix[row + 1][col] == sample_matrix[row + 1][col + 1]:
            counter_same_els += 1

print(counter_same_els)
