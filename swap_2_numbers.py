
def swap_num(a, b):
    temp = a
    a = b
    b = temp
    print(f"first number changed to {a}, second number changed to {b}")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

swap_num(number1, number2)

