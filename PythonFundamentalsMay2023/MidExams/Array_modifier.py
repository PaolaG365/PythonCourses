def swap(list_of_nums, index1, index2):
    list_of_nums[index1], list_of_nums[index2] = list_of_nums[index2], list_of_nums[index1]
    return list_of_nums


def multiply(list_of_nums, index1, index2):
    list_of_nums[index1] *= list_of_numbers[index2]
    return list_of_nums


def decrease(list_of_nums):
    list_of_nums = [num - 1 for num in list_of_nums]
    return list_of_nums


list_of_numbers = [int(x) for x in input().split()]

command = input()

while command != "end":
    command = command.split()
    action = command[0]
    event_index_1 = 0
    event_index_2 = 0

    if len(command) > 1:
        event_index_1 = int(command[1])
        event_index_2 = int(command[2])

    if action == "swap":
        list_of_numbers = swap(list_of_numbers, event_index_1, event_index_2)
    elif action == "multiply":
        list_of_numbers = multiply(list_of_numbers, event_index_1, event_index_2)
    elif action == "decrease":
        list_of_numbers = decrease(list_of_numbers)

    command = input()

print(*list_of_numbers, sep=", ")
