class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)    

    def list_books(self):
        return[f"{book.title} by {book.author}" for book in self.books ]       
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

     


library=Library('ny public library')
book_one=Book('river and the source','margaret ochola')
book_two=Book('kifp','kk')
book3 = Book("The Colour of Magic", "Terry Pratchett")
# add books in my library

library.add_book(book_one)
library.add_book(book_two)
library.add_book(book3)
print(library.name)

for book in library.list_books():
    print(book)