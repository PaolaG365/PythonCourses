def length(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def allowed_characters(password):
    if password.isalnum():
        return True
    return False


def digits_count(password):
    count_digits = 0
    for character in password:
        if character.isdigit():
            count_digits += 1

    if count_digits >= 2:
        return True
    return False


user_password = input()
if length(user_password) and allowed_characters(user_password) and digits_count(user_password):
    print("Password is valid")
if not length(user_password):
    print("Password must be between 6 and 10 characters")
if not allowed_characters(user_password):
    print("Password must consist only of letters and digits")
if not digits_count(user_password):
    print("Password must have at least 2 digits")
