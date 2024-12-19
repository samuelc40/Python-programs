
class Calculator:
    def add(self, num1, num2):
        sum = num1 + num2
        return sum

    def add_multiple(self, *args):
        sum = 0
        for arg in args:
            sum = sum + arg
        return sum
    
calc = Calculator()
ans = calc.add(23, 56)
print(ans)

ans1 = calc.add_multiple(12, 45, 34, 7, 5)
print(ans1)
