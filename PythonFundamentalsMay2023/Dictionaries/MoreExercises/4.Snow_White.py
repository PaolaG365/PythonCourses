dwarfs_ranking = {}

command = input()

while command != "Once upon a time":
    command = command.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = command[0], command[1], int(command[2])
    if dwarf_hat_color not in dwarfs_ranking:
        dwarfs_ranking[dwarf_hat_color] = {dwarf_name: dwarf_physics}
    elif dwarf_name in dwarfs_ranking[dwarf_hat_color]:
        if dwarf_physics > dwarfs_ranking[dwarf_hat_color][dwarf_name]:
            dwarfs_ranking[dwarf_hat_color][dwarf_name] = dwarf_physics
    elif dwarf_name not in dwarfs_ranking[dwarf_hat_color]:
        dwarfs_ranking[dwarf_hat_color][dwarf_name] = dwarf_physics

    command = input()

dwarf_stats = []

for hat_color, dwarf in dwarfs_ranking.items():
    for name_dwarf, score_dwarf in dwarf.items():
        dwarf_stats.append({'hat colour': hat_color, 'same hat dwarfs': len(dwarf),
                            'name dwarf': name_dwarf, 'score dwarf': score_dwarf})

dwarfs_sorted = sorted(dwarf_stats, key=lambda x: (-x['score dwarf'], -x['same hat dwarfs']))

for dwarf_rank in dwarfs_sorted:
    print(f"({dwarf_rank['hat colour']}) {dwarf_rank['name dwarf']} <-> {dwarf_rank['score dwarf']}")
