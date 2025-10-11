class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def details(self):
        return self.__str__()


class PrintBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.pages}"

    def details(self):
        return self.__str__()


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"

    def details(self):
        return self.__str__()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book.details())
