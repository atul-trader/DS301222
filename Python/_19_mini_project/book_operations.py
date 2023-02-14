from book import Book

class Operation:
    booklist = []

    def addBook(self):
        ID = int(input("Enter Book Id : "))
        name = input("Enter Book Name : ")
        edition = input("Enter Book Edition Name : ")
        publisher = input("Enter Book Publisher Name : ")
        price = float(input("Enter Book Price : "))
        book_obj = Book(ID=ID,name=name,edition=edition,publisher=publisher,price=price)
        self.booklist.append(book_obj)
        print("Book Added Successfully!")

    def viewBook(self):
        for i in self.booklist:
            print(i,"\n")

    def deleteBook(self):
        ID = int(input("Enter Book Id which you want to delete : "))
        for books in self.booklist:
            if books.get_id() == ID:
                self.booklist.remove(books)
                print("Book Successfully Deleted!")
                break
        else:
            print("Book Not Found")

    def searchBookByID(self):
        ID = int(input("Enter Book ID: "))
        for books in self.booklist:
            if books.get_id() == ID:
                print(books)
                break
        else:
            print("Book Not Found")   

    def searchBookByName(self):
        name = input("Enter name of book you want to search : ")
        for books in self.booklist:
            if books.get_name()==name:
                print(books)       
        else:
            print("Book not found")

    def updateBook(self):
        ID=int(input("Enter the ID of book you want to search : "))
        for books in self.booklist:
            if books.get_id()==ID:
                name = input("Enter Book Name : ")
                edition = input("Enter Book Edition Name : ")
                publisher = input("Enter Book Publisher Name : ")
                price = float(input("Enter Book Price : "))
                books.set_name(name)
                books.set_edition(edition)
                books.set_publisher(publisher)
                books.set_price(price)        
        else:
            print("book not found")

            