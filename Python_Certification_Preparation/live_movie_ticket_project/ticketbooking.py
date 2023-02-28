class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.user_details = {}

    def show_seats(self):
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                if i == 0 and j == 0:
                    print(" ",end=" ")
                elif j == 0:
                    print(i,end=" ")
                elif i == 0:
                    print(j,end=" ")
                else:
                    print("S",end=" ")
            print()
            

    def buy_ticket(self):
        
        row=int(input("Enter the row number for which you want to book the ticket : ")) # 1
        column=int(input("Enter the column number for which you want to book the ticket : ")) #2

        seat_no = str(row) + str(column) #12

        # TODO: Need to write the logic for front seat and back seat ticket price
        ticket_price=10

        choice = int(input(f"Your opt seat number is {seat_no}, Hence the price for your seat is Rs. {ticket_price}. If you still wish to book the ticket, please enter \n1.Yes \n2.No : \n"))
        if choice == 1:
            name=input("Enter your name : ")
            gender=input("Enter gender (Male/Female) :")
            age=int(input("Enter your age :"))
            phone_no=int(input("Enter your phone number (10 digits only) :"))
            self.user_details[seat_no] = [name,gender,age,ticket_price,phone_no]
            print("Booked Successfully!!!",self.user_details)
        else:
            print("No Problem! Thank You for connecting with Book My Show!!!")


    def statistics(self):

        ticket_price = 10
        total_seats = self.rows*self.columns
        
        no_of_tickets_booked = len(self.user_details)
        percentage_of_ticket_booked = (no_of_tickets_booked/total_seats) * 100
        current_income = no_of_tickets_booked * ticket_price
        total_income = total_seats * ticket_price

        print(f"Total number of tickets booked : {no_of_tickets_booked}")
        print(f"Percentage of booked tickets : {percentage_of_ticket_booked}")
        print(f"Current income : {current_income}")
        print(f"Total income : {total_income}")

    def get_user_info(self):
        pass

        
