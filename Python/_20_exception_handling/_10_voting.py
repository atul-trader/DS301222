from _11_custom_exception import InvalidAgeError

class Vote:
    def voting(self):
        age = int(input("Enter your age : "))
        if age >= 18:
            print("Successfully Voted!")
        else:
            try:
                raise InvalidAgeError()
                # raise print(InvalidAgeError())
            except:
                pass

obj = Vote()
obj.voting()
