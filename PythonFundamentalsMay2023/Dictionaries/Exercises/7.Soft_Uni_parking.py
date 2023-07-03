commands = int(input())
park_dict = {}

for _ in range(commands):
    command = input().split()
    event, username = command[0], command[1]

    if event == "register":
        license_plate = command[2]
        if username not in park_dict:
            park_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {park_dict[username]}")
    elif event == "unregister":
        if username not in park_dict:
            print(f"ERROR: user {username} not found")
        else:
            del park_dict[username]
            print(f"{username} unregistered successfully")

[print(f"{username} => {license_plate_number}") for username, license_plate_number in park_dict.items()]
