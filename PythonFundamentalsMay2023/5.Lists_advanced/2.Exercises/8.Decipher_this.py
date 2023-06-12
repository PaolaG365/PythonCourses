def cipher(words):
    deciphered_text = []

    for word in words:
        char_ord = ""
        second_part = ""

        for char in word:
            if char.isnumeric():
                char_ord += char
            else:
                second_part += char

        if len(second_part) > 1:
            list_second_part = [letter for letter in second_part]
            list_second_part[0], list_second_part[-1] = list_second_part[-1], list_second_part[0]
            second_part = "".join(list_second_part)

        deciphered_text.append(chr(int(char_ord)) + second_part)

    return deciphered_text


user_string = input().split()
print(" ".join(cipher(user_string)))
