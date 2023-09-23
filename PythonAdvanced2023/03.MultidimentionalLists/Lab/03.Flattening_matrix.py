from itertools import chain

lines = int(input())

sample_matrix = [[int(x) for x in input().split(', ')] for line in range(lines)]

# with itertools
flat_matrix = list(chain.from_iterable(sample_matrix))

# for cycling
# for line in sample_matrix:
#     for element in line:
#         flat_matrix.append(element)

# list comp
# flat_matrix = [element for line in sample_matrix for element in line]

# with indices
# flat_matrix = []
# for r in range(len(sample_matrix)):
#     for c in range(len(sample_matrix[r])):
#         flat_matrix.append(sample_matrix[r][c])

# with indices comprehension
# flat_matrix = [sample_matrix[r][c] for r in range(len(sample_matrix))
#                for c in range(len(sample_matrix[r]))]

print(flat_matrix)
