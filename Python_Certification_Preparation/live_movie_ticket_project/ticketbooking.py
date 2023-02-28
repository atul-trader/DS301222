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
        
        row=int(input("Enter the row number for which you want to book the ticket : "))
        column=int(input("Enter the column number for which you want to book the ticket : "))

        seat_no = str(row) + str(column) 

        total_seats = self.rows*self.columns
        
        if total_seats <= 60:
            ticket_price = 10   
        else:
            if row < (self.rows//2):
                ticket_price = 10
            else:
                ticket_price = 8
      
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

        price_lst = []
        for k,v in self.user_details.items():
            price_lst.append(v[3])

        current_income = sum(price_lst)
       
        total_seats = self.rows*self.columns
        
        if total_seats <= 60:
            total_income = total_seats * 10  
        else:
            front_price = 10
            back_price = 8
            front_seats = (self.rows//2)*self.columns
            back_seats = total_seats-front_seats
            total_income = front_seats * front_price + back_seats * back_price
          
        no_of_tickets_booked = len(self.user_details)
        percentage_of_ticket_booked = (no_of_tickets_booked/total_seats) * 100

        print(f"Total number of tickets booked : {no_of_tickets_booked}")
        print(f"Percentage of booked tickets : {percentage_of_ticket_booked}")
        print(f"Current income : {current_income}")
        print(f"Total income : {total_income}")

    def get_user_info(self):
        rows=int(input("Enter the row number of seat for which you want the info. : "))
        coloumn=int(input("Enter the coloumn number of seat for which you want the info. : "))
        
        seat_no = str(rows)+str(coloumn)

        if seat_no in self.user_details.keys():
            user = self.user_details[seat_no]
            print(f"\nName : {user[0]}")
            print(f"Gender : {user[1]}")
            print(f"Age : {user[2]}")
            print(f"Ticket Price : {user[3]}")
            print(f"Phone No. : {user[4]}\n")
        else:
            print(f"The seat number you were looking for has not been booked!!!")

        
