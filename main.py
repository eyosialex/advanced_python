import sys
from services.library_service import LibraryService

# Keep old imports for demonstration purposes
from model.book import Book
from model.ebook import Ebook
from model.student import Student
from model.bank_account import bank_account
from lesson1.inheritance import Animal, Dog
from lesson1.comp import Car, Engine
from lesson1.abstra import DogAbstract, CatAbstract

def run_lesson1_demo():
    print("\n--- Lesson 1: Abstraction, Inheritance, Composition ---")
    my_animal = Animal("walk", "grunt")
    my_animal.display()
    dog2 = Dog("run", "bark", "Bulldog")
    dog2.display()
    engine1 = Engine("V8", "Gasoline")
    car = Car(engine1, "Eyosi")
    car.display()
    
    print("\n--- Models: Book, Student, Bank Account ---")
    book1 = Book("eyosi", "fm addis", 250)
    book2 = Book("efrem", "agri", 300)
    student1 = Student("eyosi", 23, "software", 3.4)
    book1.display()
    book2.display()
    print("Student info:", student1.display())
    account = bank_account("Eyosi", 5000)
    account.deposit(1000)
    print("Balance:", account.Get_balance())
    ebook = Ebook("Eric Matthes", "Python Crash Course", 544, "25 MB")
    ebook.display()

def main():
    service = LibraryService()
    
    # Pre-populate library
    service.add_new_book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 309, "ISBN001")
    service.add_new_book("J.R.R. Tolkien", "The Hobbit", 310, "ISBN002")
    service.register_new_member("Alice")

    while True:
        print("\n=== Extensive Library Management System ===")
        print("1. Add a Book")
        print("2. Register a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. List Available Books")
        print("6. View Member Details")
        print("7. Run Old Lesson 1 Demonstrations")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            pages = int(input("Enter number of pages: "))
            isbn = input("Enter ISBN: ")
            service.add_new_book(author, title, pages, isbn)
            
        elif choice == '2':
            name = input("Enter member name: ")
            service.register_new_member(name)
            
        elif choice == '3':
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")
            service.borrow_book(member_id, isbn)
            
        elif choice == '4':
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")
            service.return_book(member_id, isbn)
            
        elif choice == '5':
            service.list_available_books()
            
        elif choice == '6':
            member_id = input("Enter Member ID: ")
            service.list_member_borrowed_books(member_id)
            
        elif choice == '7':
            run_lesson1_demo()
            
        elif choice == '8':
            print("Exiting Library Management System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()