from _2_single_inheritance import Dad

class Daughter(Dad):
    def scooty(self):
        print("Scooty")

daughter = Daughter()
daughter.scooty()
daughter.car()
daughter.flat()

