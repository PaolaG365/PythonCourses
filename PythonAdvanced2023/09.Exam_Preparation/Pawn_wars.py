ROWS, COLS = 8, 8
chess_matrix = []
letters_position = [
    [chr(char) + str(num) for char in range(ord("a"), ord("a") + COLS)]
    for num in range(ROWS, 0, -1)
]

players = {
    "White": {
        "position": [],
        "diagonals": [(-1, -1), (-1, 1)],
        "movement": (-1, 0),
        "winning row": 0,
    },
    "Black": {
        "position": [],
        "diagonals": [(1, -1), (1, 1)],
        "movement": (1, 0),
        "winning row": ROWS - 1,
    },
}
player = "Black"
winner = False


def valid_indices(index_row, index_col):
    return 0 <= index_row < ROWS and 0 <= index_col < COLS


for row in range(ROWS):
    chess_matrix.append([])
    col = 0
    for el in input().split():
        if el == "w":
            players["White"]["position"] = [row, col]
        if el == "b":
            players["Black"]["position"] = [row, col]
        col += 1
        chess_matrix[row].append(el)

while True:
    player = "White" if player == "Black" else "White"

    for diagonal in players[player]["diagonals"]:
        diagonal_row = players[player]["position"][0] + diagonal[0]
        diagonal_col = players[player]["position"][1] + diagonal[1]

        if valid_indices(diagonal_row, diagonal_col):
            if chess_matrix[diagonal_row][diagonal_col] == "w" or chess_matrix[diagonal_row][diagonal_col] == "b":
                square = letters_position[diagonal_row][diagonal_col]
                print(f"Game over! {player} win, capture on {square}.")
                winner = True
                break
    if winner:
        break

    next_row = players[player]["position"][0] + players[player]["movement"][0]
    next_col = players[player]["position"][1] + players[player]["movement"][1]
    players[player]["position"] = [next_row, next_col]

    if next_row == players[player]["winning row"]:
        square = letters_position[next_row][next_col]
        print(f"Game over! {player} pawn is promoted to a queen at {square}.")
        break
