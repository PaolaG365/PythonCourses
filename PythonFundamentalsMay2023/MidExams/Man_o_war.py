def is_valid_index(ship, section_index): return 0 <= section_index < len(ship)


def make_index_positive(ship, section_index):
    if section_index < 0:
        return len(ship) - section_index
    return section_index


def fire(government_ship, index, dmg):
    index = make_index_positive(government_ship, index)
    if is_valid_index(government_ship, index):
        government_ship[index] -= dmg
        if government_ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return government_ship


def defend(outlaws_ship, first_index, second_index, dmg):
    first_index = make_index_positive(outlaws_ship, first_index)
    second_index = make_index_positive(outlaws_ship, second_index)
    if is_valid_index(outlaws_ship, first_index) and is_valid_index(outlaws_ship, second_index):
        start_index = min(first_index, second_index)
        end_index = max(first_index, second_index)
        for section in range(start_index, end_index + 1):
            outlaws_ship[section] -= dmg
            if outlaws_ship[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return outlaws_ship


def repair(outlaws_ship, index, hp_restored):
    index = make_index_positive(outlaws_ship, index)
    if is_valid_index(outlaws_ship, index):
        outlaws_ship[index] += hp_restored
        if outlaws_ship[index] > max_hp_section:
            outlaws_ship[index] = max_hp_section
    return outlaws_ship


def status(outlaws_ship):
    threshold_hp = max_hp_section * 0.2
    sections_needing_repair = [num for num in outlaws_ship if num < threshold_hp]
    return f"{len(sections_needing_repair)} sections need repair."


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(k) for k in input().split(">")]
max_hp_section = int(input())

command = input()

while command != "Retire":
    command = command.split()
    action = command[0]
    index1 = 0
    index2_or_num = 0
    # action, *data = [int(x) if x[-1].isdigit() else x for x in command.split()]
    if len(command) >= 2:
        index1, index2_or_num = int(command[1]), int(command[2])

    if action == "Fire":
        war_ship = fire(war_ship, index1, index2_or_num)
    elif action == "Defend":
        damage = int(command[3])
        pirate_ship = defend(pirate_ship, index1, index2_or_num, damage)
    elif action == "Repair":
        pirate_ship = repair(pirate_ship, index1, index2_or_num)
    elif action == "Status":
        print(status(pirate_ship))

    command = input()

else:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}")
