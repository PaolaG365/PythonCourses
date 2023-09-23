lines_input = int(input())
sample_matrix = []

# sample_matrix = [[int(x) for x in input().split()] for _ in range(lines_input)]
# diagonal_sum = 0
# for el_index in range(lines_input):
#     diagonal_sum += sample_matrix[el_index][el_index]
# print(diagonal_sum)

diagonal_sum = 0
for index1 in range(lines_input):
    sample_matrix.append([int(x) for x in input().split()])
    diagonal_sum += sample_matrix[index1][index1]
print(diagonal_sum)
