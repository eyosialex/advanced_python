class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.isbn not in [b.isbn for b in self.borrowed_books]:
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        for b in self.borrowed_books:
            if b.isbn == book.isbn:
                self.borrowed_books.remove(b)
                return True
        return False

    def display(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print("Borrowed Books:")
        if not self.borrowed_books:
            print("  None")
        else:
            for b in self.borrowed_books:
                print(f"  - {b.title} ({b.isbn})")
