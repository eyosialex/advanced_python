class Book:
    def __init__(self,author,title,page):
        self.author=author;
        self.title=title;
        self.page=page;
    def display(self):
        print("author: "+self.author)
        print ("title: "+self.title)
        print("page: ",self.page)
    def is_big(self):
        return self.page>500

        