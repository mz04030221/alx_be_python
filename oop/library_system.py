class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "Book"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return super().__str__()

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return super().__str__()

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            book_type = type(book).__name__
            print(f"{book_type}: {book.title} by {book.author}", end="")
            
            if book_type == "EBook":
                print(f", File Size: {book.file_size}KB")
            elif book_type == "PrintBook":
                print(f", Page Count: {book.page_count}")
            else:
                print()

