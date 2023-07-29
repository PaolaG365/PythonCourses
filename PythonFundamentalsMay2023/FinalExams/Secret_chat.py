def insert_space(text, target_index): return text[:target_index] + " " + text[target_index:]


def reverse(text, target_string):
    first_occurrence = text.find(target_string)
    if first_occurrence >= 0:
        text = text[:first_occurrence] + text[first_occurrence + len(target_string):] + target_string[::-1]
        print(text)
    else:
        print("error")
    return text


def change_all(text, first_string, second_string): return text.replace(first_string, second_string)


concealed_message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        concealed_message = insert_space(concealed_message, index)
        print(concealed_message)
    elif action == "Reverse":
        substring = command[1]
        concealed_message = reverse(concealed_message, substring)
    elif action == "ChangeAll":
        substring, replacement_string = command[1], command[2]
        concealed_message = change_all(concealed_message, substring, replacement_string)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
