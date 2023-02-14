from book_operations import Operation

class Main:

    def execute(self,choice,operation):
        if choice == 1:
            print("******Add Book*******")
            operation.addBook()

        if choice == 2:
            print("******View Book******")


if __name__ == "__main__":
    
    operation = Operation()
    main = Main()
    while True:
        choice = int(input("Enter \n1.Add Book \n2.View Book \n3.Delete Book : \n"))
        main.execute(choice=choice,operation=operation)