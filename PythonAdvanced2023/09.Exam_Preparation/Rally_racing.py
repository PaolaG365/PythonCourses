moves = {"left": [0, -1], "right": [0, 1], "down": [1, 0], "up": [-1, 0]}

rows_racetrack = int(input())
racecar_number = input()
kilometers_passed = 0
car_pos = [0, 0]
tunnels_pos = []
track_matrix = []

for row_trace in range(rows_racetrack):
    col_trace = 0
    track_matrix.append([])
    for el in input().split():
        if el == "T":
            tunnels_pos.append((row_trace, col_trace))
        track_matrix[row_trace].append(el)
        col_trace += 1

command = input()
while command != "End":
    next_row = car_pos[0] + moves[command][0]
    next_col = car_pos[1] + moves[command][1]
    next_pos = track_matrix[next_row][next_col]

    if next_pos == "T":
        kilometers_passed += 30
        track_matrix[next_row][next_col] = "."
        tunnels_pos.remove((next_row, next_col))
        track_matrix[tunnels_pos[0][0]][tunnels_pos[0][1]] = "."
        car_pos = [tunnels_pos[0][0], tunnels_pos[0][1]]

    elif next_pos == "F":
        print(f"Racing car {racecar_number} finished the stage!")
        car_pos = [next_row, next_col]
        kilometers_passed += 10
        break
    else:
        car_pos = [next_row, next_col]
        kilometers_passed += 10

    command = input()
else:
    print(f"Racing car {racecar_number} DNF.")

track_matrix[car_pos[0]][car_pos[1]] = "C"
print(f"Distance covered {kilometers_passed} km.")
[print(*track, sep="") for track in track_matrix]
