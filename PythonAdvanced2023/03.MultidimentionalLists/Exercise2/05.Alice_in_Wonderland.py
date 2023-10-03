alice_info = {
    'position': [],
    'collected tea bags': 0,
}

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


wonderland_matrix = []
alice_lost = False

rows = int(input())
for r in range(rows):
    wonderland_matrix.append(input().split())
    if 'A' in wonderland_matrix[r]:
        alice_info['position'] = [r, wonderland_matrix[r].index('A')]
        wonderland_matrix[r][alice_info['position'][1]] = '*'

while True:
    direction = input()
    next_row = alice_info['position'][0] + moves[direction][0]
    next_col = alice_info['position'][1] + moves[direction][1]

    if are_valid_indices(next_row, next_col, wonderland_matrix):
        if wonderland_matrix[next_row][next_col].isdigit():
            alice_info['collected tea bags'] += int(wonderland_matrix[next_row][next_col])
        elif wonderland_matrix[next_row][next_col] == "R":
            alice_lost = True
        alice_info['position'] = [next_row, next_col]
        wonderland_matrix[next_row][next_col] = '*'
    else:
        alice_lost = True

    if alice_info['collected tea bags'] >= 10:
        print("She did it! She went to the party.")
        break

    if alice_lost:
        print("Alice didn't make it to the tea party.")
        break

[print(*line) for line in wonderland_matrix]
