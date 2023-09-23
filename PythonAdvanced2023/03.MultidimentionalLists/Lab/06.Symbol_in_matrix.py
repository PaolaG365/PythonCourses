lines = int(input())

sample_matrix = [[el for el in input()] for _ in range(lines)]
searched_symbol = input()

counter = 0
for row in sample_matrix:
    if searched_symbol in row:
        print(f"({counter}, {row.index(searched_symbol)})")
        break
    counter += 1
else:
    print(f"{searched_symbol} does not occur in the matrix")

# with indices
#
# for row_index in range(len(sample_matrix)):
#     for col_index in range(len(sample_matrix[row_index])):
#         if sample_matrix[row_index][col_index] == searched_symbol:
#             print(f"({row_index}, {col_index})")
#             exit()
#
# print(f"{searched_symbol} does not occur in the matrix")
