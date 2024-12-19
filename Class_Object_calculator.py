class Calculator:
    def addition(self, num1, num2):
        return num1 + num2

    def substraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2

calc = Calculator()

print("Welcome to the calculator program")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Please select an operation: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = calc.addition(num1, num2)
    print("The sum of your entered numbers is : ",result)

elif choice == 2:
    result = calc.substraction(num1, num2)
    print("The result of your entered number is : ",result)

elif choice == 3:
    result = calc.multiplication(num1,num2)
    print("The result of your entered number is : ",result)

elif choice == 4:
    result = calc.division(num1,num2)
    print("The result of your entered number is : ",result)

else:
    print("Try to select from the operations next time!!!")