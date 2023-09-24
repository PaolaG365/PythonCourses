def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


arithmetic_actions = {
    'Add': lambda x, y: x + y,
    'Subtract': lambda x, y: x - y,
}

rows = int(input())
sample_matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    action, row, col, num = [int(x) if x.lstrip('-').isdigit() else x for x in command.split()]

    if are_valid_indices(row, col, sample_matrix):
        sample_matrix[row][col] = arithmetic_actions[action](sample_matrix[row][col], num)
    else:
        print("Invalid coordinates")

    command = input()

[print(*line) for line in sample_matrix]
