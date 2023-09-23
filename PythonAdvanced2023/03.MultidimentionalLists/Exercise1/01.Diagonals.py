rows = int(input())

sample_matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for ind in range(rows):
    primary_diagonal.append(sample_matrix[ind][ind])

for ind in range(rows):
    secondary_diagonal.append(sample_matrix[ind][len(sample_matrix[ind]) - ind - 1])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. "
      f"Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. "
      f"Sum: {sum(secondary_diagonal)}")
