rows, cols = [int(x) for x in input().split()]

sample_matrix = [input().split() for _ in range(rows)]


def are_valid_indices(index1, index2, matrix):
    if 0 <= index1 < len(matrix):
        if 0 <= index2 < len(matrix[index1]):
            return True
    return False


command = input()
while command != "END":
    data = command.split()
    if len(data) != 5 or data[0] != "swap":
        print("Invalid input!")
    else:
        row1, col1 = int(data[1]), int(data[2])
        row2, col2 = int(data[3]), int(data[4])
        if are_valid_indices(row1, col1, sample_matrix) and are_valid_indices(row2, col2, sample_matrix):
            sample_matrix[row1][col1], sample_matrix[row2][col2] =\
             sample_matrix[row2][col2], sample_matrix[row1][col1]
            [print(*matrix) for matrix in sample_matrix]
        else:
            print("Invalid input!")

    command = input()
