class Book:

    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def borrow (self):
        if self.is_available:
            print (f"'{self.title}' is available")
        else:
            print (f"'{self.title}' is not available")

    def return_book (self):
        if self.is_available:
            print (f"'{self.title}' is already on the shelf.")
        else:
            print (f"Thank you for returning '{self.title}'")

    def get_info (self):
        print (f"-----'{self.title}' by {self.author}-----")
        print (f"           isbn: {self.isbn}")

book1 = Book ("Daffodils", "William Wordsworth", "123456789", False)
book2 = Book ("Atomic Habits", "James Clear", "147852369", False)
book3 = Book ("The Muslim Scientist", "Bu Ali Sina", "987654321", True)
book4 = Book ("The Hobbit", "Clever Flemming", "159264837", True)

class Library:
    total_books = 0

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1

    def show_available_books(self):
        for book in self.books:
            if book.is_available:
                print(book)


    def find_book_by_title(self, title):
        for book in self.books:
            if title == book.title:
                return book
        return None

Library1 = Library ()
Library1.add_book(book1)
Library1.add_book(book2)
Library1.add_book(book3)
Library1.add_book(book4)

Library1.show_available_books()