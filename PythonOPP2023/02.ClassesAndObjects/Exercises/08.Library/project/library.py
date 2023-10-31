from typing import List, Dict
from user import User


class Library:

    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # {author: list of books}
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for rented_books in self.rented_books.values():  # check if its rented
            if book_name in rented_books:
                return (f'The book "{book_name}" is already rented and will be available in '
                        f'{rented_books[book_name]} days!')

        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            self.rented_books.setdefault(user.username, {})
            self.rented_books[user.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        del self.rented_books[user.username][book_name]
        self.books_available[author].append(book_name)
