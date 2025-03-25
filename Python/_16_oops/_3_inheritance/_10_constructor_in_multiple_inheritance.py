class c_lang:
    def __init__(self):
        print("C")

    def procedural_feature(self):
        print("Procedural Feature")

class cpp_lang:
    def __init__(self):
        print("CPP")

    def oops_feature(self):
        print("OOPs Feature")

class python(c_lang,cpp_lang):
    def __init__(self):
        # super().__init__()
        c_lang.__init__(self)
        cpp_lang.__init__(self)
        print("Python")

    def both(self):
        print("Both features")


py_obj = python()
py_obj.procedural_feature()
py_obj.oops_feature()
py_obj.both()

