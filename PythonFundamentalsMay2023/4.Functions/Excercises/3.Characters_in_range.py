def chars_in_range(a, b):
    list_of_chars = []
    for char in range(ord(a) + 1, ord(b)):
        list_of_chars.append(chr(char))
    return list_of_chars


first_char, second_char = input(), input()
print(" ".join(chars_in_range(first_char, second_char)))
