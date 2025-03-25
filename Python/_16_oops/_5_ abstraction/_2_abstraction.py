from abc import ABC,abstractmethod

class College(ABC):

    def timing(self):
        return "10am - 1pm"

    @abstractmethod
    def exam_ticket(self):
        pass


class ClassA(College):
    def exam_ticket(self):
        return "IT Exam Ticket"

class ClassB(College):
    def exam_ticket(self):
        return "CS Exam Ticket"

class ClassC(College):
    def exam_ticket(self):
        return "BSC Exam Ticket"

classa = ClassA()
classb = ClassB()
classc = ClassC()

print(classa.timing())
print(classa.exam_ticket())

print(classb.timing())
print(classb.exam_ticket())

print(classc.timing())
print(classc.exam_ticket())