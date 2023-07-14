def character_multiplier(string1, string2):
    total_sum = 0
    for index in range(len(string1)):
        if index < len(string2):
            total_sum += (ord(string1[index]) * ord(string2[index]))
        else:
            total_sum += ord(string1[index])
    return total_sum


list_of_strings = input().split()

if len(list_of_strings[0]) >= len(list_of_strings[1]):
    print(character_multiplier(list_of_strings[0], list_of_strings[1]))
elif len(list_of_strings[0]) < len(list_of_strings[1]):
    print(character_multiplier(list_of_strings[1], list_of_strings[0]))
