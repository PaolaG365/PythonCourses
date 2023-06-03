people_in_circle = input().split()
initial_counter = int(input())
suicide_order = []
counter = initial_counter
first_removed = True
human_to_remove = 0

while len(people_in_circle) > 0:

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

result = ",".join(suicide_order)

print("[" + result + "]")
