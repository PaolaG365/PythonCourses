user_string_to_remove = input()
string_to_clean = input()


while user_string_to_remove in string_to_clean:
    string_to_clean = string_to_clean.replace(user_string_to_remove, "")

print(string_to_clean)
