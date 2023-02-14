from book import Book

class Operation:

    def addBook(self):
        self.booklist = []
        ID = int(input("Enter Book Id : "))
        name = input("Enter Book Name : ")
        edition = input("Enter Book Edition Name : ")
        publisher = input("Enter Book Publisher Name : ")
        price = float(input("Enter Book Price : "))
        book_obj = Book(ID=ID,name=name,edition=edition,publisher=publisher,price=price)
        self.booklist.append(book_obj)
        print("Book Added Successfully!")

    def viewBook(self):
        pass