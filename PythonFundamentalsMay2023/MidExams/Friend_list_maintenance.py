def is_valid_index(targets, index):
    if len(targets) - 1 >= index >= 0:
        return True
    return False


def blacklisted(user_names, counter, name):
    if name in user_names:
        name_index = user_names.index(name)
        user_names.remove(name)
        user_names.insert(name_index, "Blacklisted")
        print(f"{name} was blacklisted.")
        counter += 1
        return user_names, counter
    else:
        print(f"{name} was not found.")
    return user_names, counter


def error(user_names, counter, index):
    if is_valid_index(user_names, index):
        if user_names[index] != "Lost" and user_names[index] != "Blacklisted":
            name = user_names.pop(index)
            user_names.insert(index, "Lost")
            counter += 1
            print(f"{name} was lost due to an error.")
            return user_names, counter
    return user_names, counter


def change(user_names, index, new_user_name):
    if is_valid_index(user_names, index):
        if user_names[index] != "Lost" or user_names[index] != "Blacklisted":
            previous_user_name = user_names.pop(index)
            user_names.insert(index, new_user_name)
            print(f"{previous_user_name} changed his username to {new_user_name}.")
            return user_names
    return user_names


names_list = input().split(", ")
command = input()
blacklisted_counter = 0
lost_counter = 0

while command != "Report":
    command = command.split()
    action = command[0]

    if action == "Blacklist":
        index_or_name = command[1]
        names_list, blacklisted_counter = blacklisted(names_list, blacklisted_counter, index_or_name)
    elif action == "Error":
        index_or_name = int(command[1])
        names_list, lost_counter = error(names_list, lost_counter, index_or_name)
    elif action == "Change":
        index_or_name = int(command[1])
        user_name = command[2]
        names_list = change(names_list, index_or_name, user_name)

    command = input()

print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {lost_counter}")
print(" ".join(names_list))
