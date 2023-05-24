fav_book = input()

checked_books_count = 0

while True:
    checked_book = input()

    if checked_book == "No More Books":
        print(f'The book you search is not here!\nYou checked {checked_books_count} books.')
        break

    checked_books_count += 1

    if checked_book == fav_book:
        print(f"You checked {checked_books_count - 1} books and found it.")
        break
