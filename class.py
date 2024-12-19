
class Test:
    var = 30
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        # a = 20
        print("I'm a function", self.name, self.age)

obj = Test('Samuel', 22)
print(obj.var)

obj.func()

print(obj.name)
print(obj.age)


