def take_odd(text): return text[1::2]  # odd indices of string


def cut(text, start_index, taken_indices): return text[:start_index] + text[start_index + taken_indices:]


def substitute(text, string_to_remove, new_string):
    if string_to_remove in text:
        text = text.replace(string_to_remove, new_string)
        print(text)
    else:
        print("Nothing to replace!")
    return text


password = input()

command = input()

while command != "Done":
    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        password = take_odd(password)
        print(password)
    elif action == "Cut":
        index, length = int(command[1]), int(command[2])
        password = cut(password, index, length)
        print(password)
    elif action == "Substitute":
        substring, substitute_string = command[1], command[2]
        password = substitute(password, substring, substitute_string)

    command = input()

print(f"Your password is: {password}")
