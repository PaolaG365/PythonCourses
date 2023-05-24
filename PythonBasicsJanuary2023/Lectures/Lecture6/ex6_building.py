floors_building, room_building = int(input()), int(input())

for f in range(floors_building, 0, -1):

    for r in range(0, room_building):
        if f == floors_building:
            print(f"L{f}{r} ", end='')
        elif f % 2 == 0:
            print(f"O{f}{r} ", end='')
        else:
            print(f"A{f}{r} ", end='')
    print()
