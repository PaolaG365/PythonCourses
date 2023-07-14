list_of_strings = input().split()

for index in range(len(list_of_strings)):
    list_of_strings[index] = list_of_strings[index] * len(list_of_strings[index])

print("".join(list_of_strings))
