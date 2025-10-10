# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)   # call the Book constructor
        self.file_size = file_size

    def details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)   # call the Book constructor
        self.page_count = page_count

    def details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # this is composition — the library *has* books

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book, EBook or PrintBook instances can be added.")
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.details())
