info = {
    'player_position': [],
    'available_targets': [],
    'shot_targets': [],
}

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


shooting_field = []

for index_row in range(5):
    shooting_field.append([])
    count = 0
    for el in input().split():
        if el == "A":
            info['player_position'] = [index_row, count]
        if el == "x":
            info['available_targets'].append((index_row, count))
        shooting_field[index_row].append(el)
        count += 1


commands = int(input())
for _ in range(commands):
    command = input().split()
    action, direction = command[0], command[1]

    if action == "move":
        steps = int(command[2])
        shooting_field[info['player_position'][0]][info['player_position'][1]] = "."
        next_row = info['player_position'][0]
        next_col = info['player_position'][1]
        if direction == "up" or direction == "down":
            next_row = info['player_position'][0] + steps * moves[direction][0]
        else:
            next_col = info['player_position'][1] + steps * moves[direction][1]
        if are_valid_indices(next_row, next_col, shooting_field):
            if shooting_field[next_row][next_col] == ".":
                info['player_position'] = [next_row, next_col]

    elif action == "shoot":
        shot_row = info['player_position'][0] + moves[direction][0]
        shot_col = info['player_position'][1] + moves[direction][1]
        for shot in range(5):
            if are_valid_indices(shot_row, shot_col, shooting_field):
                if shooting_field[shot_row][shot_col] == "x":
                    shooting_field[shot_row][shot_col] = "."
                    info['available_targets'].remove((shot_row, shot_col))
                    info['shot_targets'].append([shot_row, shot_col])
                    break
                shot_row += moves[direction][0]
                shot_col += moves[direction][1]
            else:
                break

    if not info['available_targets']:
        print(f"Training completed! All {len(info['shot_targets'])} targets hit.")
        break
else:
    print(f"Training not completed! {len(info['available_targets'])} targets left.")

print(*info['shot_targets'], sep='\n')
