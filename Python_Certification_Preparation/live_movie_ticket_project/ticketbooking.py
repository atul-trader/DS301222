class movie_ticket:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns

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
        pass
    
        
