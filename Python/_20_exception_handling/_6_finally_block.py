try:
    print(10/0)
except TypeError as ex:
    print(ex)
finally:
    print("Finally Block")

# finally block - code gets executed even when exception is handled or it is not handled

