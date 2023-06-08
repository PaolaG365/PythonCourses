def string_without_vowels(words):
    vowels = ["a", "o", "u", "e", "i"]
    return [letter for letter in words if letter.lower() not in vowels]


user_string = input()
print("".join(string_without_vowels(user_string)))
