class grandpa:
    def field(self):
        print("Field")


class dad(grandpa):
    def flat(self):
        print("Flat")


class child(dad):
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")


child_obj = child()
child_obj.bike()
child_obj.mobile()
child_obj.flat()
child_obj.field()
