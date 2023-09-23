rows = int(input())

sample_matrix = [[int(x) for x in input().split()] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for ind in range(rows):
    primary_diagonal.append(sample_matrix[ind][ind])

for ind in range(rows):
    secondary_diagonal.append(sample_matrix[ind][-ind - 1])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
