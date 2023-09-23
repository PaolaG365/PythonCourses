rows_n, cols_n = [int(x) for x in input().split(', ')]

sample_matrix = [[int(x) for x in input().split()] for el in range(rows_n)]

# for col in range(cols_n):
#     column_sum = 0
#     for row in range(rows_n):
#         column_sum += sample_matrix[row][col]
#     print(column_sum)

cols_sum = [sum([sample_matrix[r][c] for r in range(rows_n)]) for c in range(cols_n)]
print(*cols_sum, sep="\n")

# look ma it works
# print(*[sum([sample_matrix[r][c] for r in range(rows_n)]) for c in range(cols_n)], sep='\n')
