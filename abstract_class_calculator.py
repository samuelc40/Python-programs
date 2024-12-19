# Write a program to include all the functionalities of ta calculator using ABSTRACT class and
# abstract method. All the methods (add, sub, mul, div) should be inside of abstract class.
# Abstract method definition should be another class.


from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self, x, y):
        pass
    @abstractmethod
    def sub(self, x, y):
        pass
    @abstractmethod
    def mul(self, x, y):
        pass
    @abstractmethod
    def div(self, x, y):
        pass

class BasicCalculator(Calculator):
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y
    def mul(self, x, y):
        return x*y
    def div(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divided by Zero!!!")
        return x/y
obj = BasicCalculator()
print(obj.add(3, 4))
print(obj.sub(3, 4))
print(obj.mul(3, 4))
print(obj.div(3, 4))