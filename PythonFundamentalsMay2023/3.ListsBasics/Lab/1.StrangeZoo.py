first_string = input()
second_string = input()
third_string = input()
list_in_order = [first_string, second_string, third_string]

list_in_order[0], list_in_order[2] = list_in_order[2], list_in_order[0]

print(list_in_order)
