class exception:

    def div(self):
        print(10/0)

    def division(self):
        self.div()

obj = exception()
obj.division()