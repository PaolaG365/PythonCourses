force_book = {}
force_user_and_side = input()


def is_force_user_in_force_book(book, human_name):
    for value_book in book.values():
        for side_user in value_book:
            if human_name == side_user:
                return True
    return False


while force_user_and_side != "Lumpawaroo":
    force_user, user_side = "", ""

    if "|" in force_user_and_side:
        user_side, force_user = force_user_and_side.split(" | ")
        if user_side not in force_book:
            force_book[user_side] = []
        if not is_force_user_in_force_book(force_book, force_user):
            force_book[user_side].append(force_user)

    elif "->" in force_user_and_side:
        force_user, user_side = force_user_and_side.split(" -> ")
        if user_side not in force_book:
            force_book[user_side] = []

        if is_force_user_in_force_book(force_book, force_user):
            force_side = ""
            for side, users in force_book.items():
                for user in users:
                    if user == force_user:
                        force_side = side
            force_book[force_side].remove(force_user)
            force_book[user_side].append(force_user)
        elif not is_force_user_in_force_book(force_book, force_user):
            force_book[user_side].append(force_user)

        print(f"{force_user} joins the {user_side} side!")

    force_user_and_side = input()

for key, value in force_book.items():
    if value:
        print(f"Side: {key}, Members: {len(value)}")
        [print(f"! {user_of_force_side}") for user_of_force_side in force_book[key]]
