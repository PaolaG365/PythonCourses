def existing_piece(dictionary, name):
    if name in dictionary:
        return True
    else:
        print(f"Invalid operation! {name} does not exist in the collection.")
        return False


def add_piece(dictionary, name, author, music_key):
    if name in dictionary:
        print(f"{name} is already in the collection!")
    else:
        dictionary[name] = {'composer': author, 'key': music_key}
        print(f"{name} by {author} in {music_key} added to the collection!")
    return dictionary


def remove_piece(dictionary, name):
    if existing_piece(dictionary, name):
        del dictionary[name]
        print(f"Successfully removed {name}!")
    return dictionary


def change_key(dictionary, name, music_key):
    if existing_piece(dictionary, name):
        dictionary[name]['key'] = music_key
        print(f"Changed the key of {name} to {music_key}!")
    return dictionary


lines = int(input())

compositions_data = {}

for info in range(lines):
    piece, composer, key = input().split("|")
    if piece not in compositions_data:
        compositions_data[piece] = {}
    compositions_data[piece].update({'composer': composer, 'key': key})

command = input()

while command != "Stop":
    command = command.split("|")
    action, piece_name = command[0], command[1]

    if action == "Add":
        name_composer, key_music = command[2], command[3]
        compositions_data = add_piece(compositions_data, piece_name, name_composer, key_music)
    elif action == "Remove":
        compositions_data = remove_piece(compositions_data, piece_name)
    elif action == "ChangeKey":
        new_key = command[2]
        compositions_data = change_key(compositions_data, piece_name, new_key)

    command = input()

for piece_info, data in compositions_data.items():
    print(f"{piece_info} -> Composer: {data['composer']}, Key: {data['key']}")
