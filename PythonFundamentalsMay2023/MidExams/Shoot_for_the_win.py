def shot_target(list_of_target, index, eliminated):
    eliminated_target = list_of_target[index]
    list_of_target[index] = - 1
    eliminated += 1

    for num in range(len(list_of_target)):
        if list_of_target[num] == - 1:
            continue
        elif list_of_target[num] <= eliminated_target:
            list_of_target[num] += eliminated_target
        else:
            list_of_target[num] -= eliminated_target

    return list_of_target, eliminated


targets = [int(x) for x in input().split()]
target = input()
targets_shot = 0

while target != "End":
    target = int(target)
    if len(targets) - 1 >= target >= 0:
        targets, targets_shot = shot_target(targets, target, targets_shot)

    target = input()

print(f"Shot targets: {targets_shot} ->", *targets)
