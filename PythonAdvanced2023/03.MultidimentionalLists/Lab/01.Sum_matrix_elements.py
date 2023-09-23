rows_n, cols_n = [int(x) for x in input().split(", ")]

sample_matrix = []
sum_matrix = 0

for row in range(rows_n):
    line_matrix = [int(x) for x in input().split(", ")]
    sample_matrix.append(line_matrix)
    sum_matrix += sum(line_matrix)

print(sum_matrix)
print(sample_matrix)
