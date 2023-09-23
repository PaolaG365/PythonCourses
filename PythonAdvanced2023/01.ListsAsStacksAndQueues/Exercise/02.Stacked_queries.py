from collections import deque


numbers_list = deque()
number_of_commands = int(input())

map_functions = {
    1: lambda x: numbers_list.append(x[1]),
    2: lambda x: numbers_list.pop() if numbers_list else None,
    3: lambda x: print(max(numbers_list)) if numbers_list else None,
    4: lambda x: print(min(numbers_list)) if numbers_list else None
}

for command in range(number_of_commands):
    action = [int(x) for x in input().split()]
    map_functions[action[0]](action)

numbers_list.reverse()
print(*numbers_list, sep=", ")


'''
numbers_list = []
stack = []
number_of_commands = int(input())

for command in range(number_of_commands):
    action = input().split()
    if len(action) > 1:
        numbers_list.append(int(action[1]))
    elif action[0] == '2':
        if numbers_list:
            numbers_list.pop()
    elif action[0] == '3':
        if numbers_list:
            print(max(numbers_list))
    elif action[0] == '4':
        if numbers_list:
            print(min(numbers_list))

while numbers_list:
    stack.append(numbers_list.pop())
print(*stack, sep=", ")
'''