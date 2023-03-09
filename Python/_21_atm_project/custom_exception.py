class InvalidDataTypeError(Exception):
    def __init__(self):
        print("InvalidDataTypeError: Pin should only have digits or length is less than 4")
        
class InvalidLengthError(Exception):
    def __init__(self):
        print("InvalidLengthError: PIN should have exactly 4 digits")

class ReseverdPin(Exception):
    def __init__(self):
        print(f"ReservedPin Error: Entered pin does not matches the stored pin.")

class DepositlimitError(Exception):
    def __init__(self):
        print("Amount should be less than 25000 Rupees")
        
class InvalidDepositError(Exception):
    def __init__(self):
        print("Amount should be in multiples of 100")
        
class WithdrawallimitError(Exception):
    def __init__(self):
        print("Amount should be less than 25000 Rupees")
        
class InvalidwithdrawalError(Exception):
    def __init__(self):
        print("Amount should be in multiples of 100")