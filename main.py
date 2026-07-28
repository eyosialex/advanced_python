from model.book import Book
from model.ebook import Ebook
from model.student import Student
from model.bank_account import bank_account
def main():
    book1=Book("eyosi","fm addis")
  
    book2=Book("efrem","agri",)
    
    student1= Student("eyosi",23,"software",3.4)
    print ("the available books ")
    book1.display()
    
    book2.display()
    Book.check_page(560)
    print ( "my big book is: ")
    book1.is_big()
    print( "total books :" ,Book.totalbook)
    print("student info :" ,student1.display())
    account = bank_account(
        "Eyosi",
        5000
    )


    account.deposit(1000)

    account.withdraw(2000)


    print(
        "Balance:",
        account.Get_balance()
    )
    ebook = Ebook(
        "Eric Matthes",
        "Python Crash Course",
        544,
        "25 MB"
    )
    ebook.display()


if __name__=="__main__":
         main()