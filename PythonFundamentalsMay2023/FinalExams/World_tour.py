def is_valid_index(text, n): return True if 0 <= n <= len(text) - 1 else False


def add_stop(text, num, stop):
    if is_valid_index(text, num):
        text = text[0:num] + stop + text[num:]
    return text


def remove_stop(text, num1, num2):
    if is_valid_index(text, num1) and is_valid_index(text, num2):
        first_index = min(num1, num2)
        second_index = max(num1, num2)
        text = text[0:first_index] + text[second_index + 1:]
    return text


def switch(text, string1, string2): return text.replace(string1, string2)


travel_stops = input()

command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        target_stop = command[2]
        travel_stops = add_stop(travel_stops, index, target_stop)
        print(travel_stops)

    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        travel_stops = remove_stop(travel_stops, start_index, end_index)
        print(travel_stops)

    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        travel_stops = switch(travel_stops, old_string, new_string)
        print(travel_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {travel_stops}")
