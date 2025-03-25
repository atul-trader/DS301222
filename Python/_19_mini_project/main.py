from book_operations import Operation

class Main:

    def execute(self,choice,operation):
        if choice == 1:
            print("******Add Book*******")
            operation.addBook()

        if choice == 2:
            print("******View Book******")
            operation.viewBook()

        if choice == 3:
            print("********Delete Book******")
            operation.deleteBook()

        if choice == 4:
            print("********Seach Book By ID******")
            operation.searchBookByID()

        if choice == 5:
            print("********Seach Book By Name******")
            operation.searchBookByName()

        if choice == 6:
            print("********Update Book******")
            operation.updateBook()

         

if __name__ == "__main__":
    
    operation = Operation()
    main = Main()
    while True:
        choice = int(input("Enter \n1.Add Book \n2.View Book \n3.Delete Book \n4.Search Book By ID \n5.Search Book By Name \n6.Update Book : \n"))
        main.execute(choice=choice,operation=operation)