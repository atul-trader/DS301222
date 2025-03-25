# Abstraction
# showing the functionality and hiding the implementation

# Abstract Methods
# methods without body
# with decorator 'abstractmethod'

# Abstract Class
# a class with atleast one abstract method
# we cannot create the object of abstract class
# it can have abstract / instance methods

from abc import abstractmethod,ABC

class Laptop(ABC):
    @abstractmethod
    def motherboard(self):
        pass

    def keyboard(self):
        print("Keyboard helps in typing")

class Programmer(Laptop):
    def motherboard(self):
        print("Motherboard")

programmer = Programmer()
programmer.keyboard()
programmer.motherboard()