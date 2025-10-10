# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: runs when a Book is created.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor: runs when a Book object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Human-friendly string (used by print()).
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string that could recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
