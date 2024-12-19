class First:
    def display(self):
        print("First class")

class Second():
    def display(self):
        print("Second class")

class Third(Second,First):
    def display(self):
        print("Third class")

x=Third()
# x.display()
x.display()

print(Third.mro())