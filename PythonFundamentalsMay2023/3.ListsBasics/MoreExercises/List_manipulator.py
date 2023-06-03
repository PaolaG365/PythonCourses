integer_list = input().split()
integer_list = [int(x) for x in integer_list]

command = input()

while command != "end":
    list_of_command = command.split()

    even_numbers = [x for x in integer_list if x % 2 == 0]
    odd_numbers = [x for x in integer_list if x % 2 != 0]

    if "exchange" in list_of_command:
        index_to_change = int(list_of_command[1])
        if len(integer_list) > index_to_change >= 0:
            integer_list = integer_list[index_to_change + 1:] + integer_list[:index_to_change + 1]
        else:
            print("Invalid index")

    elif "max" in list_of_command:
        if "even" in list_of_command:
            if even_numbers:
                max_even = max(even_numbers)
                print(len(integer_list) - integer_list[::-1].index(max_even) - 1)
            else:
                print("No matches")

        elif "odd" in list_of_command:
            if odd_numbers:
                max_odd = max(odd_numbers)
                print(len(integer_list) - integer_list[::-1].index(max_odd) - 1)
            else:
                print("No matches")

    elif "min" in list_of_command:
        if "even" in list_of_command:
            if even_numbers:
                min_even = min(even_numbers)
                print(len(integer_list) - integer_list[::-1].index(min_even) - 1)
            else:
                print("No matches")

        elif "odd" in list_of_command:
            if odd_numbers:
                min_odd = min(odd_numbers)
                print(len(integer_list) - integer_list[::-1].index(min_odd) - 1)
            else:
                print("No matches")

    elif "first" in list_of_command:
        count = int(list_of_command[1])

        if count > len(integer_list):
            print("Invalid count")
        elif "even" in list_of_command:
            print(even_numbers[:count])
        elif "odd" in list_of_command:
            print(odd_numbers[:count])

    elif "last" in list_of_command:
        count = int(list_of_command[1])

        if count > len(integer_list):
            print("Invalid count")
        elif "even" in list_of_command:
            print(even_numbers[-count:])
        elif "odd" in list_of_command:
            print(odd_numbers[-count:])

    command = input()

print(integer_list)
