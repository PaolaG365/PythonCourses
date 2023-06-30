string_list = [char for char in input() if char != " "]
string_dict = {}

for symbol in string_list:
    if symbol not in string_dict:
        string_dict[symbol] = 0
    string_dict[symbol] += 1

[print(f"{char} -> {occurrences}") for char, occurrences in string_dict.items()]
