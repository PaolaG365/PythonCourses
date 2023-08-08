def valid_item(shopping_list, shopping_item): return True if shopping_item in shopping_list else False


def urgent(shopping_list, shopping_item):
    if not valid_item(shopping_list, shopping_item):
        shopping_list.insert(0, shopping_item)
    return shopping_list


def unnecessary(shopping_list, shopping_item):
    if valid_item(shopping_list, shopping_item):
        shopping_list.remove(shopping_item)
    return shopping_list


def correct(shopping_list, shopping_item, new_shopping_item):
    if valid_item(shopping_list, shopping_item):
        target_index = shopping_list.index(shopping_item)
        shopping_list[target_index] = new_shopping_item
    return shopping_list


def rearrange(shopping_list, shopping_item):
    if valid_item(shopping_list, shopping_item):
        shopping_list.remove(shopping_item)
        shopping_list.append(shopping_item)
    return shopping_list


list_with_groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split()
    action, item = command[0], command[1]

    if action == "Urgent":
        list_with_groceries = urgent(list_with_groceries, item)
    elif action == "Unnecessary":
        list_with_groceries = unnecessary(list_with_groceries, item)
    elif action == "Correct":
        new_item = command[2]
        list_with_groceries = correct(list_with_groceries, item, new_item)
    elif action == "Rearrange":
        list_with_groceries = rearrange(list_with_groceries, item)

    command = input()

print(", ".join(list_with_groceries))
