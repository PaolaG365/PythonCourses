def find_index(index1, index2):
    first = min(index1, index2)
    second = max(index1, index2)
    return first, second


def contains(text, words):
    if words in text:
        return f"{text} contains {words}"
    else:
        return f"Substring not found!"


def flip_to_lower_or_upper(text, low_or_up, first_index, second_index):
    first_index, second_index = find_index(first_index, second_index)
    target_text = ""
    if low_or_up == "Upper":
        target_text = "".join([char.upper() for char in text[first_index:second_index]])
    elif low_or_up == "Lower":
        target_text = "".join([char.lower() for char in text[first_index:second_index]])
    text = text[:first_index] + target_text + text[second_index:]
    print(text)
    return text


def slice_string(text, first_index, second_index):
    first_index, second_index = find_index(first_index, second_index)
    text = text[:first_index] + text[second_index:]
    print(text)
    return text


raw_activation_key = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        print(contains(raw_activation_key, substring))
    elif action == "Flip":
        flip_to, start_index, end_index = command[1], int(command[2]), int(command[3])
        raw_activation_key = flip_to_lower_or_upper(raw_activation_key, flip_to, start_index, end_index)
    elif action == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        raw_activation_key = slice_string(raw_activation_key, start_index, end_index)

    command = input()

print(f"Your activation key is: {raw_activation_key}")
