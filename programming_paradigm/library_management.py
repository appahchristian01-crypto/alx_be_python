# library_management.py

class Book:
    def __init__(self, title, author):
        # public attributes
        self.title = title
        self.author = author
        # private attribute to track checked-out status
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out. Return True if successful."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned. Return True if successful."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        # private list to store Book instances
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Find a book by title and check it out if available.
        Returns True if checkout succeeded, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Find a book by title and return it if it was checked out.
        Returns True if return succeeded, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        """Print each available book exactly as: Title by Author"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
