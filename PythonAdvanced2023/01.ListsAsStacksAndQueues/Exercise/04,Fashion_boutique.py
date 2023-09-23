from collections import deque

clothes_packages = deque([int(x) for x in input().split()])
rack_capacity = int(input())

rack, racks_counter = 0, 1

while clothes_packages:
    if rack + clothes_packages[-1] <= rack_capacity:
        rack += clothes_packages.pop()
    else:
        rack = 0
        racks_counter += 1

print(racks_counter)
