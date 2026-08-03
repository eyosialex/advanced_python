class Book:
    totalbook = 0

    def __init__(self, author, title, page, isbn=None):
        self.author = author
        self.title = title
        self.page = page
        self.isbn = isbn
        self.available = True
        Book.totalbook += 1

    def display(self):
        print(f"ISBN: {self.isbn}")
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Pages: {self.page}")
        print(f"Status: {'Available' if self.available else 'Borrowed'}")

    def is_big(self):
        return self.page > 500

    def borrow(self):
        if self.available:
            self.available = False
            Book.totalbook -= 1
            print(f"Success: '{self.title}' has been borrowed.")
            return True
        else:
            print(f"Error: '{self.title}' is already borrowed.")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            Book.totalbook += 1
            print(f"Success: '{self.title}' has been returned.")
            return True
        else:
            print(f"Info: '{self.title}' was not borrowed.")
            return False

    @classmethod
    def get_total_books(cls):
        print(f"Total available books: {cls.totalbook}")
        return cls.totalbook

    @staticmethod
    def check_page(page):
        if page > 500:
            print("large")
        else:
            print("medium")