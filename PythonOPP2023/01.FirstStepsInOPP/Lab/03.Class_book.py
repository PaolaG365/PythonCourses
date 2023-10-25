class Book:

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


# samples
book1 = Book("My Book", "Me", 200)
print(book1.name)
print(book1.author)
print(book1.pages)

book2 = Book("Harry Potter and The Deadly Hallows", "J.K. Rowlling", 759)
print(book2.name)
print(book2.author)
print(book2.pages)
