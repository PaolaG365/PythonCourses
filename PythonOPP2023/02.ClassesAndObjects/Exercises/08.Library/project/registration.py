from library import Library
from user import User


class Registration:

    @staticmethod
    def add_user(user: User, library: Library) -> str:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library) -> str:
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return ("Please check again the provided username - it should be different"
                            " than the username used so far!")

                if user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books[user.username]
                    del library.rented_books[user.username]

                user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"
