import re

decryption_keys = [int(x) for x in input().split()]
max_index_keys = len(decryption_keys) - 1

encrypted_message = [symbol for symbol in input()]

treasure = re.compile(r"&.+&")
location = re.compile(r"<.+>")

while encrypted_message != "find":
    index_key = 0
    encrypted_message = [symbol for symbol in encrypted_message]

    for index in range(len(encrypted_message)):
        encrypted_message[index] = chr(ord(encrypted_message[index]) - decryption_keys[index_key])
        index_key += 1
        if index_key > max_index_keys:
            index_key = 0

    decrypted_message = "".join(encrypted_message)
    type_of_treasure = re.search(treasure, decrypted_message)
    treasure_location = re.search(location, decrypted_message)
    print(f"Found {type_of_treasure.group().strip('&')} at {treasure_location.group().strip('<>')}")
    encrypted_message = input()
