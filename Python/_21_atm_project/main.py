from custom_exception import *

stored_pin = 1234
balance = 50000
pin = 0
choice = 0

try:
    pin = int(input("Enter your pin (in digits only): "))
except ValueError:
    print("Wrong Value")
    exit(0)

if not(pin > 999 and pin < 10000):
    try:
        raise InvalidDataTypeError() 
    except:
        exit(0)

if pin != stored_pin:
    try:
        raise ReseverdPin()
    except:
        exit(0)

while True:
    try:
        choice = int(input("Enter \n1.Deposit \n2.Withdrawal \n3.Mini-Statement \n:"))
    except ValueError:
        print("Wrong Value")
        exit(0)

    if choice == 1:
        amount = int(input("Enter the amount to deposit : "))
        if amount>25000:
            try:
                raise DepositlimitError()
            except:
                pass
        if not(amount % 100) == 0 or amount < 100 :
            try:
                raise InvalidDepositError()
            except:
                pass
        balance = balance + amount
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw : "))
        if amount>25000:
            try:
                raise WithdrawallimitError()
            except:
                pass
        if not(amount % 100) == 0 or  amount < 100 :
            try:
                raise InvalidwithdrawalError()
            except:
                pass
        balance = balance - amount
    elif choice == 3:
        print("Available Balance : ",balance)
    else:
        print("Bye")

    
# Enter your pin:

# 1. Deposit
# enter amount
# 2. Withdraw
# enter amount
# 3. Mini-Statement