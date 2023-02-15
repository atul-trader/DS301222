try:
    print(10/0)
    str1 = None
    print(len(str1))
except TypeError as ex:
    print("TypeError")
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
except FileNotFoundError as ex:
    print("FileNotFoundError")
except Exception as ex:
    print("Exception")
