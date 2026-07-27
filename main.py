from model.book import Book
from model.student import Student
def main():
    book1=Book("eyosi","fm addis",78)
    book2=Book("efrem","agri",560)
    student1= Student("eyosi",23,"software",3.4)
    print ("the available books ")
    book1.display()
    
    book2.display()
    Book.check_page(560)
    print ( "my big book is: ")
    book1.is_big()
    print( "total books :" ,Book.totalbook)
    print("student info :" ,student1.display())

if __name__=="__main__":
         main()