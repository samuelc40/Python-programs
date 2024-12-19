class BaseClass:
    def __init__(self):
        print("Base init")

    def set_name(self,name):
        self.name=name
        print("Baseclass set name")

class SubClass(BaseClass):

    def __init__(self):
        super().__init__()
        print("Subclass init")

    def set_name(self,name):
        super().set_name(name)
        print("Subclass set name")

    def welcome(self):
        print("Welcome")

    def display_name(self):
        print("Name : " + self.name)

y=SubClass()
y.welcome()
y.set_name("Samuel Joseph")
y.display_name()