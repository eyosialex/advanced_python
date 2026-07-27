from model.book import Book
from model.student import Student
def main():
    book1=  Book("eyosi","fm addis",78)
    student1= Student("eyosi",23,"software",3.4)
    print ("the available books ")
    book1.display()
    book1.borrow()
    book1.display()
    print ( "my big book is: ")
    book1.is_big()
    print("student info :" ,student1.display())

if __name__=="__main__":
         main()