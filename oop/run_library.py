from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library instance
    my_library = Library()

    # Create different types of books
    book1 = Book("Pride and Prejudice", "Jane Austen")
    book2 = EBook("Snow Crash", "Neal Stephenson", 500)
    book3 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Display all books in the library
    my_library.display_books()

if __name__ == "__main__":
    main()
