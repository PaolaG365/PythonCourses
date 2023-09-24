# a whole novel...  a radioactive vampire bunnies apocalypse novel

game_info = {
    'player_position': [],
    'bunnies_position': [],
    'spreading_pos': [],
}

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

maze_matrix = []
game_over = False
player_won = False


def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


# bunnies spread obv...
def bunny_explosion(matrix, game_o):
    if game_info['spreading_pos']:
        game_info['bunnies_position'] = game_info['spreading_pos']
        game_info['spreading_pos'] = []

    for vampire_bunny in game_info['bunnies_position']:
        vb_row, vb_col = vampire_bunny

        for spread_pattern in moves.values():
            hop_row = vb_row + spread_pattern[0]
            hop_col = vb_col + spread_pattern[1]

            if are_valid_indices(hop_row, hop_col, matrix) and matrix[hop_row][hop_col] != 'P' and\
               matrix[hop_row][hop_col] != "B":

                matrix[hop_row][hop_col] = "B"
                game_info['spreading_pos'].append((hop_row, hop_col))

            elif are_valid_indices(hop_row, hop_col, matrix) and matrix[hop_row][hop_col] == 'P':
                matrix[hop_row][hop_col] = "B"
                game_o = True

    return matrix, game_o


def game_turn(move, sample_matrix, game_o, got_out):
    player_row, player_col = game_info['player_position']
    next_row = player_row + moves[move][0]
    next_col = player_col + moves[move][1]

    if (are_valid_indices(next_row, next_col, sample_matrix) and
            sample_matrix[next_row][next_col] != 'B'):
        sample_matrix[next_row][next_col], sample_matrix[player_row][player_col] = \
         sample_matrix[player_row][player_col], sample_matrix[next_row][next_col]
        game_info['player_position'] = [next_row, next_col]

    elif (are_valid_indices(next_row, next_col, sample_matrix) and
          sample_matrix[next_row][next_col] == 'B') and not game_o:
        game_info['player_position'] = [next_row, next_col]
        game_o = True

    elif not are_valid_indices(next_row, next_col, sample_matrix):
        sample_matrix[player_row][player_col] = "."
        got_out = True

    sample_matrix, game_o = bunny_explosion(sample_matrix, game_o)

    return sample_matrix, game_o, got_out


rows, cols = [int(x) for x in input().split()]

for index_row in range(rows):
    maze_matrix.append([])
    count = 0
    for el in input():
        if el == "P":
            game_info['player_position'] = [index_row, count]
        if el == "B":
            game_info['bunnies_position'].append((index_row, count))
        maze_matrix[index_row].append(el)
        count += 1

player_moves = [el for el in input()]

for player_move in player_moves:
    if game_over or player_won:
        break
    maze_matrix, game_over, player_won = game_turn(player_move, maze_matrix, game_over, player_won)

[print(*maze_line, sep='') for maze_line in maze_matrix]

if player_won:
    print(f"won: ", end="")
    print(*game_info['player_position'])

if game_over:
    print(f"dead: ", end="")
    print(*game_info['player_position'])
