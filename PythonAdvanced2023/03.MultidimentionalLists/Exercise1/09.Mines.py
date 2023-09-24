game_info = {
    'miner_position': [],
    'coal_count': 0,
}

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


def miners_game(command, matrix):
    miner_row, miner_col = game_info['miner_position']
    next_step_row = miner_row + moves[command][0] if miner_row + moves[command][0] > 0 else 0
    next_step_col = miner_col + moves[command][1] if miner_col + moves[command][1] > 0 else 0

    if are_valid_indices(next_step_row, next_step_col, matrix):
        found_el = matrix[next_step_row][next_step_col]

        if found_el == 'c':
            game_info['coal_count'] -= 1
            matrix[next_step_row][next_step_col] = '*'

            if game_info['coal_count'] == 0:
                print(f"You collected all coal! ({next_step_row}, {next_step_col})")
                exit()

        elif found_el == 'e':
            print(f"Game over! ({next_step_row}, {next_step_col})")
            exit()

        game_info['miner_position'] = [next_step_row, next_step_col]

    return matrix


rows_mine = int(input())
commands = input().split()

matrix_mine = []

for index_row in range(rows_mine):
    row = input().split()
    matrix_mine.append(row)
    if 's' in row:
        game_info['miner_position'] = [index_row, row.index('s')]
    if 'c' in row:
        game_info['coal_count'] += row.count('c')

for com in commands:
    matrix_mine = miners_game(com, matrix_mine)

print(f"{game_info['coal_count']} pieces of coal left. "
      f"({game_info['miner_position'][0]}, {game_info['miner_position'][1]})")
