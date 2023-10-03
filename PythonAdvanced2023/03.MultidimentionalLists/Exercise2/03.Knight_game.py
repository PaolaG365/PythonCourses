knight_moves = [
    (-2, 1), (-2, -1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

board_matrix = []
knights_positions_on_board = []
removed_knights_counter = 0


def are_valid_indices(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[index1])


# wrote the func first and then discovered i have to call it someway, somehow
# so it took a turn to recursion out of laziness...
def find_knight_with_max_attacks(r_knights_counter):
    max_knight_attacks = 0
    max_k_pos = ()
    for knight_row, knight_col in knights_positions_on_board:
        current_knight_attacks = 0
        for move_row, move_col in knight_moves:
            next_row = knight_row + move_row
            next_col = knight_col + move_col
            if are_valid_indices(next_row, next_col, board_matrix) and \
                    board_matrix[next_row][next_col] == "K":
                current_knight_attacks += 1
        if current_knight_attacks > max_knight_attacks:
            max_knight_attacks = current_knight_attacks
            max_k_pos = (knight_row, knight_col)

    if max_knight_attacks and max_k_pos:
        r_knights_counter += 1
        knights_positions_on_board.remove((max_k_pos[0], max_k_pos[1]))
        board_matrix[max_k_pos[0]][max_k_pos[1]] = "0"
        return find_knight_with_max_attacks(r_knights_counter)
    else:
        return r_knights_counter


num_lines = int(input())
for row in range(num_lines):
    board_matrix.append([])
    count = 0
    for el in input():
        if el == "K":
            knights_positions_on_board.append((row, count))
        board_matrix[row].append(el)
        count += 1

print(find_knight_with_max_attacks(removed_knights_counter))
