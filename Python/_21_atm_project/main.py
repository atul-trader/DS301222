stored_pin = "1234"

pin = input("Enter your pin: ")

if not pin.isdigit():
    raise Exception("The entered pin should only contain digits.")

if len(pin) != 4:
    raise Exception("The entered pin should be exactly 4 digits.")

if pin != stored_pin:
    raise Exception("The entered pin does not match the stored pin.")
    