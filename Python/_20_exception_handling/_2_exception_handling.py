class exception:
    def div(self):
        div = 0
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        try:
            div = no1/no2
        except Exception as ex:
            print("Exception have been raised : ",ex)
        print("Addition : ",div)
        print("End of program!")

obj = exception()
obj.div()

# Two Blocks
# try ---> to store suspicous code
# except ---> to store handling code, if exception is raised