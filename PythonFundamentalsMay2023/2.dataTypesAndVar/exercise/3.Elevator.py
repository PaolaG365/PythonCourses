import math
group_people = int(input())
capacity_elevator = int(input())

# courses_needed = group_people // capacity_elevator
#
# if group_people % capacity_elevator != 0:
#     courses_needed += 1

print(math.ceil(group_people / capacity_elevator))
