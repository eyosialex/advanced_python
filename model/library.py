class Library:
    def __init__(self):
        self.books = {}     # Dictionary mapping ISBN to Book object
        self.members = {}   # Dictionary mapping member_id to Member object

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            return True
        return False

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False

    def add_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            return True
        return False

    def get_book(self, isbn):
        return self.books.get(isbn)

    def get_member(self, member_id):
        return self.members.get(member_id)

    def find_books_by_title(self, title):
        return [book for book in self.books.values() if title.lower() in book.title.lower()]