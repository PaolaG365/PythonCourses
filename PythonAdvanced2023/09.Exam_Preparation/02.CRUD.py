moves = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}
game_matrix = []

for row in range(6):
    game_matrix.append(input().split())

current_row, current_col = [int(x) for x in input() if x.isdigit()]

command = input()
while command != "Stop":
    command = command.split(", ")
    action, direction = command[0], command[1]
    next_row = current_row + moves[direction][0]
    next_col = current_col + moves[direction][1]

    if action == "Create":
        value = command[2]
        if game_matrix[next_row][next_col] == ".":
            game_matrix[next_row][next_col] = value

    elif action == "Update":
        value = command[2]
        if game_matrix[next_row][next_col] != ".":
            game_matrix[next_row][next_col] = value

    elif action == "Delete":
        if game_matrix[next_row][next_col] != ".":
            game_matrix[next_row][next_col] = "."
    elif action == "Read":

        if game_matrix[next_row][next_col] != ".":
            print(game_matrix[next_row][next_col])
    current_row, current_col = next_row, next_col
    command = input()

[print(*line) for line in game_matrix]
