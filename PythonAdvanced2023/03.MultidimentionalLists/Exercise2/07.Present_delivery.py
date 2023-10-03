christmas_info = {
    "Santa coordinates": [],
    "nice kids number": 0,
    "happy nice kids": 0
}

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

presents_count = int(input())
size_neighborhood = int(input())
neighborhood_matrix = []

for row in range(size_neighborhood):
    neighborhood_matrix.append([])
    count = 0
    for el in input().split():
        if el == "S":
            christmas_info["Santa coordinates"] = [row, count]
        if el == "V":
            christmas_info["nice kids number"] += 1
        neighborhood_matrix[row].append(el)
        count += 1

direction = input()

while direction != "Christmas morning":
    next_row = christmas_info["Santa coordinates"][0] + moves[direction][0]
    next_col = christmas_info["Santa coordinates"][1] + moves[direction][1]

    if 0 <= next_row < size_neighborhood and 0 <= next_col < size_neighborhood:

        if neighborhood_matrix[next_row][next_col] == "C":
            for move in moves.values():
                gift_giving_row = next_row + move[0]
                gift_giving_col = next_col + move[1]

                if neighborhood_matrix[gift_giving_row][gift_giving_col] == "V":
                    presents_count -= 1
                    christmas_info["happy nice kids"] += 1
                elif neighborhood_matrix[gift_giving_row][gift_giving_col] == "X":
                    presents_count -= 1

                neighborhood_matrix[gift_giving_row][gift_giving_col] = "-"

        elif neighborhood_matrix[next_row][next_col] == "V":
            presents_count -= 1
            christmas_info["happy nice kids"] += 1

        neighborhood_matrix[christmas_info["Santa coordinates"][0]][christmas_info["Santa coordinates"][1]] = "-"
        christmas_info["Santa coordinates"] = [next_row, next_col]
        neighborhood_matrix[next_row][next_col] = "S"

    if christmas_info["nice kids number"] == christmas_info["happy nice kids"]:
        break
    if presents_count <= 0 and christmas_info["nice kids number"] > christmas_info["happy nice kids"]:
        print("Santa ran out of presents!")
        break

    direction = input()

[print(*street) for street in neighborhood_matrix]

if christmas_info["nice kids number"] > christmas_info["happy nice kids"]:
    print(f"No presents for {christmas_info['nice kids number'] - christmas_info['happy nice kids']} nice kid/s.")
else:
    print(f"Good job, Santa! {christmas_info['happy nice kids']} happy nice kid/s.")
