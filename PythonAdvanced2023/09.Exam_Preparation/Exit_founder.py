game_info = {
    1: {"player name": "", "row": 0, "col": 0, "rest": False},
    2: {"player name": "", "row": 0, "col": 0, "rest": False},
}

game_info[1]["player name"], game_info[2]["player name"] = input().split(", ")
current_player = 2
game_matrix = [input().split() for _ in range(6)]

while True:
    current_player = 2 if current_player == 1 else 1
    game_info[current_player]["row"], game_info[current_player]["col"] = [int(x) for x in input()
                                                                          if x.isdigit()]

    if game_info[current_player]["rest"]:
        game_info[current_player]["rest"] = False
        continue

    next_step = game_matrix[game_info[current_player]["row"]][game_info[current_player]["col"]]

    if next_step == "W":
        print(f"{game_info[current_player]['player name']} hits a wall and needs to rest.")
        game_info[current_player]["rest"] = True
    if next_step == "E":
        print(f"{game_info[current_player]['player name']} found the Exit and wins the game!")
        break
    if next_step == "T":
        print(f"{game_info[current_player]['player name']} is out of the game! ", end="")
        current_player = 2 if current_player == 1 else 1
        print(f"The winner is {game_info[current_player]['player name']}.")
        break
