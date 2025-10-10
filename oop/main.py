from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)            # uses __str__
    print(repr(my_book))      # uses __repr__
    del my_book               # triggers __del__

if __name__ == "__main__":
    main()
