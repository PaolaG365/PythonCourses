def office_chairs(n):
    chairs = 0
    visitors = 0
    rooms = {}  # room number - chairs needed

    for room in range(1, n + 1):
        command = input().split()
        chairs += int(len(command[0]))
        visitors += int(command[1])

        if len(command[0]) < int(command[1]):
            rooms.update({room: (int(command[1]) - len(command[0]))})

    return chairs, visitors, rooms


number_of_rooms = int(input())
chairs_in_office, visitors_in_office, needed_chairs_in_room = office_chairs(number_of_rooms)

if not needed_chairs_in_room:
    print(f"Game On, {chairs_in_office - visitors_in_office} free chairs left")
else:
    for el in range(len(needed_chairs_in_room)):
        room_number = list(needed_chairs_in_room)[el]
        chairs_needed = list(needed_chairs_in_room.values())[el]
        print(f"{chairs_needed} more chairs needed in room {room_number}")
