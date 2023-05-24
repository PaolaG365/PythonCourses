players_disqualified = input()
disqualified_list = players_disqualified.split(" ")
GAME_TERMINATED = False
A_TEAM = 11
B_TEAM = 11

for player in set(disqualified_list):
    if "A" in player:
        A_TEAM -= 1
    if "B" in player:
        B_TEAM -= 1

    if A_TEAM < 7 or B_TEAM < 7:
        GAME_TERMINATED = True
        break

print(f"Team A - {A_TEAM}; Team B - {B_TEAM}")

if GAME_TERMINATED:
    print("Game was terminated")
