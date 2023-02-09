class Mom:
    def jewellery(self):
        print("Jewellery")

    def land(self):
        print("Land")

    def mobile(self):
        print("Mom's Mobile")

class Dad:
    def flat(self):
        print("Flat")

    def mobile(self):
        print("Dad's Mobile")

class Son(Dad,Mom):
    def bike(self):
        print("Mobile")

    def mobile(self):
        print("Son's Mobile")
        

son = Son()
son.bike()
son.jewellery()
son.flat()
son.land()
son.mobile()

print(Son.mro()) # MRO -> Method Resolution Order

