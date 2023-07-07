challengers = {}
challengers_total_points = {}

command = input()

while command != "Season end":
    if " -> " in command:
        command = command.split(" -> ")
        player, position, skill_points = command[0], command[1], int(command[2])
        if player not in challengers:
            challengers[player] = {position: skill_points}
        elif position not in challengers[player]:
            challengers[player].update({position: skill_points})
        elif skill_points > challengers[player][position]:
            challengers[player][position] = skill_points

    elif " vs " in command:
        player1, player2 = command.split(" vs ")

        if player1 in challengers and player2 in challengers:
            player1_lanes = set(challengers[player1].keys())
            player2_lanes = set(challengers[player2].keys())
            # finds if there is any common lanes between players through intersection in sets
            if player1_lanes & player2_lanes:
                player1_total_skill_points = sum(challengers[player1].values())
                player2_total_skill_points = sum(challengers[player2].values())
                # you are demoted...
                if player1_total_skill_points > player2_total_skill_points:
                    del challengers[player2]
                elif player2_total_skill_points > player1_total_skill_points:
                    del challengers[player1]

    command = input()

# rank em
for challenger, skills in challengers.items():
    total_skill_points_challenger = sum(challengers[challenger].values())
    challengers_total_points.update({challenger: total_skill_points_challenger})

final_ranking = sorted(challengers_total_points.items(), key=lambda x: (-x[1], x))

for noob, total_skills in final_ranking:
    print(f"{noob}: {total_skills} skill")
    sorted_lanes_by_points = sorted(challengers[noob].items(), key=lambda x: (-x[1], x))
    for lane, score in sorted_lanes_by_points:
        print(f"- {lane} <::> {score}")
