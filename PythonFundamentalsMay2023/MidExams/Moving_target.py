def shoot(targets_list, index, power):
    if is_valid_index(targets_list, index):
        targets_list[index] -= power
        if targets_list[index] <= 0:
            targets_list.pop(index)

    return targets_list


def add(targets, index, value):
    if is_valid_index(targets, index):
        targets.insert(index, value)
    else:
        print("Invalid placement!")

    return targets


def strike(targets, index, radius):
    if is_valid_index(targets, index) and is_valid_index(targets, index + radius)\
          and is_valid_index(targets, index - radius):
        targets = targets[:index - radius] + targets[index + radius + 1:]
    else:
        print("Strike missed!")

    return targets


def is_valid_index(targets, index):
    if len(targets) - 1 >= index >= 0:
        return True
    return False


sequence_targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command = command.split()
    action = command[0]
    index_target = int(command[1])
    number = int(command[2])

    if action == "Shoot":
        sequence_targets = shoot(sequence_targets, index_target, number)
    elif action == "Add":
        sequence_targets = add(sequence_targets, index_target, number)
    elif action == "Strike":
        sequence_targets = strike(sequence_targets, index_target, number)

    command = input()

print(*sequence_targets, sep="|")
