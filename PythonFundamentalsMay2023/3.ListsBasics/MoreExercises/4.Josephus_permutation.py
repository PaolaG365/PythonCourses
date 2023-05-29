people_in_circle = input().split()
initial_counter = int(input())
suicide_order = []
counter = initial_counter
first_removed = True
human_to_remove = 0

while len(people_in_circle) > 0:

    #     # human_removed = ((len(people_in_circle) - 1) + initial_counter) % len(people_in_circle)
    #     # suicide_order.append(people_in_circle.pop(human_removed))
    #     for human in range(len(people_in_circle)):
    #         counter -= 1
    #         if counter == 1:
    #             suicide_order.append(people_in_circle.pop(human))
    #     # suicide_order = [int(x) for x in suicide_order]
    if first_removed:
        first_removed = False
        for human in people_in_circle:
            if counter == 1:
                people_in_circle.remove(human)
                suicide_order.append(human)
        counter -= 1
    else:
        human_to_remove = ((human_to_remove + initial_counter - 1) % len(people_in_circle))
        suicide_order.append(people_in_circle.pop(human_to_remove))

# suicide_order = [int(x) for x in suicide_order]
result = ",".join(suicide_order)

print("[" + result + "]")
