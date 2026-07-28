from model.book import Book
class Ebook(Book):
    def __init__(self,author ,title,pages,file_size):
        super().__init__(author,title,pages)
        self.file_size=file_size