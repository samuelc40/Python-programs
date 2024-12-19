
class Parent:
    def func(self):
        print("I'm a parent function...")

class Child(Parent):
    def func(self):
        super().func()
        print("I'm a child function...")

obj = Child()
obj.func()
