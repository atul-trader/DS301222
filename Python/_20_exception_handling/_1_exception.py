# Exception - unwanted/unexpected event
# Exception Handling - finding an alternate way to gracefully terminate the flow

class exception:
    def div(self):
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        div = no1/no2
        print("Addition : ",div)
        print("End of program!")

obj = exception()
obj.div()