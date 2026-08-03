from model.library import Library
from model.book import Book
from model.members import Member

class LibraryService:
    def __init__(self):
        self.library = Library()
        self.next_member_id = 1

    def register_new_member(self, name):
        member_id = f"M{self.next_member_id:03d}"
        new_member = Member(member_id, name)
        self.library.add_member(new_member)
        self.next_member_id += 1
        print(f"Member '{name}' registered successfully with ID: {member_id}")
        return member_id

    def add_new_book(self, author, title, page, isbn):
        new_book = Book(author, title, page, isbn)
        if self.library.add_book(new_book):
            print(f"Book '{title}' added to the library with ISBN: {isbn}")
            return True
        else:
            print(f"Error: A book with ISBN {isbn} already exists.")
            return False

    def borrow_book(self, member_id, isbn):
        member = self.library.get_member(member_id)
        book = self.library.get_book(isbn)

        if not member:
            print(f"Error: Member ID {member_id} not found.")
            return False
        if not book:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        if book.borrow():
            member.borrow_book(book)
            print(f"{member.name} successfully borrowed '{book.title}'.")
            return True
        return False

    def return_book(self, member_id, isbn):
        member = self.library.get_member(member_id)
        book = self.library.get_book(isbn)

        if not member:
            print(f"Error: Member ID {member_id} not found.")
            return False
        if not book:
            print(f"Error: Book with ISBN {isbn} not found.")
            return False

        if book.return_book():
            member.return_book(book)
            print(f"{member.name} successfully returned '{book.title}'.")
            return True
        return False

    def list_available_books(self):
        print("\n--- Available Books ---")
        available_books = [b for b in self.library.books.values() if b.available]
        if not available_books:
            print("No books are currently available.")
        else:
            for b in available_books:
                print(f"- {b.title} by {b.author} (ISBN: {b.isbn})")

    def list_member_borrowed_books(self, member_id):
        member = self.library.get_member(member_id)
        if not member:
            print(f"Error: Member ID {member_id} not found.")
            return
        member.display()
