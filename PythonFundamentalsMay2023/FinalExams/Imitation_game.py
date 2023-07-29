def move(text, number_letters):
    if 0 <= number_letters - 1 < len(text):
        text = text[number_letters:] + text[0:number_letters]
    return text


def insert_in_string(text, target_index, new_letters):
    if 0 <= target_index <= len(text):
        text = text[0:target_index] + new_letters + text[target_index:]
    return text


def change_all(text, first_string, second_string):
    if first_string in text:
        text = text.replace(first_string, second_string)
    return text


message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        message = move(message, number_of_letters)

    elif action == "Insert":
        index, value = int(command[1]), command[2]
        message = insert_in_string(message, index, value)

    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        message = change_all(message, substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
