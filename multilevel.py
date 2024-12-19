
class GrandParent:
    print("Grand parent class...")
    def func(self):
        a = 10
        print(a)

class Parent(GrandParent):
    print("Parent class...")

class Child(Parent):
    print("Child class...")

obj = Child()
obj.func()