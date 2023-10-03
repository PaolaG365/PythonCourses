info = {
    'bunny position': [],
    'hops coordinates with max gain': [],
    'direction max gain': '',
    'easter eggs collected': 0
}

moves = {'up': (-1, 0), 'left': (0, -1), 'right': (0, 1), 'down': (1, 0)}


def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


easter_matrix = []

rows = int(input())
for row in range(rows):
    easter_matrix.append([int(el) if el.lstrip('-').isdigit() else el for el in input().split()])
    if "B" in easter_matrix[row]:
        info['bunny position'] = [row, easter_matrix[row].index("B")]

for direction, possible_r_c in moves.items():
    hops_position = []
    current_gains = 0
    current_bunny_pos = info['bunny position']

    for hop in range(rows):
        next_hop_row = current_bunny_pos[0] + possible_r_c[0]
        next_hop_col = current_bunny_pos[1] + possible_r_c[1]

        if not are_valid_indices(next_hop_row, next_hop_col, easter_matrix) or \
           easter_matrix[next_hop_row][next_hop_col] == "X":
            break

        current_gains += easter_matrix[next_hop_row][next_hop_col]
        hops_position.append([next_hop_row, next_hop_col])
        current_bunny_pos = [next_hop_row, next_hop_col]

    if current_gains >= info['easter eggs collected']:
        info['easter eggs collected'] = current_gains
        info['direction max gain'] = direction
        info['hops coordinates with max gain'] = hops_position


print(info['direction max gain'])
[print(coordinate) for coordinate in info['hops coordinates with max gain']]
print(info['easter eggs collected'])
