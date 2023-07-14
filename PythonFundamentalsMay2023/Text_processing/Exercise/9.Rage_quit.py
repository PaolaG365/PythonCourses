rage_message_to_deliver = input()
string_to_repeat = ""
new_string = ""
repeat_count = ""

for index in range(len(rage_message_to_deliver)):
    if not rage_message_to_deliver[index].isdigit():
        string_to_repeat += rage_message_to_deliver[index]
    else:
        for next_symbols in range(index, len(rage_message_to_deliver)):
            if not rage_message_to_deliver[next_symbols].isdigit():
                break
            else:
                repeat_count += rage_message_to_deliver[next_symbols]
        new_string += string_to_repeat.upper() * int(repeat_count)
        string_to_repeat = ""
        repeat_count = ""

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
