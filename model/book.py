class Book:
    totalbook=0;
    def __init__(self,author,title,page):
        self.author=author;
        self.title=title;
        self.page=page;
        self.available=True
        Book.totalbook=Book.totalbook+1;
    # @property
    # def page(self):
    #     return self.__page
    # @page.setter
    # def page( self ,value ):
    #     if value >0:
    #         self.__page=value
    #     else :
    #         print( "pages must be positive ")


    def display(self):
        print("author: "+self.author)
        print ("title: "+self.title)
        print("page: ",self.page)
    def is_big(self):
        return self.page>500
    def borrow (self):
        if self.available:
            self.available=False
            Book.totalbook-=1
            print (f"print the book is borrow ")
        else:
            print(f"print the book is already borrowed")
    def return_book(self):
        self.available=true
        self.totalbook+=1
        print ( "the book {self.name} has ben returned")
    @classmethod
    def get_total_books(cls):
        return print("totalbook: ",cls.totalbook) 
    @staticmethod
    def check_page(page):
        if page >500 :
            print("large")
        else :
            print("miduem")


        