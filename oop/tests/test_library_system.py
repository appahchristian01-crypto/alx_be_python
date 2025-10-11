# tests/test_library_system.py
import sys
import os
import pytest

# Ensure the parent folder (oop/) is on sys.path so `library_system` can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from library_system import Book, EBook, PrintBook, Library

def test_book_initialization():
    book = Book("Pride and Prejudice", "Jane Austen")
    assert book.title == "Pride and Prejudice"
    assert book.author == "Jane Austen"
    assert isinstance(book, Book)

def test_ebook_initialization():
    ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    assert ebook.title == "Snow Crash"
    assert ebook.author == "Neal Stephenson"
    assert ebook.file_size == 500
    assert isinstance(ebook, EBook)
    assert isinstance(ebook, Book)

def test_printbook_initialization():
    pbook = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    assert pbook.title == "The Catcher in the Rye"
    assert pbook.author == "J.D. Salinger"
    assert pbook.page_count == 234
    assert isinstance(pbook, PrintBook)
    assert isinstance(pbook, Book)

def test_details_return_expected_strings():
    book = Book("Pride and Prejudice", "Jane Austen")
    ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    pbook = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    assert book.details() == "Book: Pride and Prejudice by Jane Austen"
    assert ebook.details() == "EBook: Snow Crash by Neal Stephenson, File Size: 500KB"
    assert pbook.details() == "PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234"

def test_library_add_book_accepts_and_rejects():
    lib = Library()
    book = Book("Test", "Author")
    lib.add_book(book)
    assert lib.books[-1] is book

    with pytest.raises(TypeError):
        lib.add_book("not a book")
