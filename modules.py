
# num = int(input("Enter a number to find the factorial: "))

def factorial(n):

    result = 1

    if n < 0:
        print("Factorial is not findable for this number!")
    else:
        for i in range(1, n + 1):
            result *= i
        print(result)

def operations(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    print(f"The sum of {num1} and {num2} is: {add}")
    print(f"The substraction of {num1} and {num2} is: {sub}")
    print(f"The multiplication of {num1} and {num2} is: {mul}")
    print(f"The division of {num1} and {num2} is: {div}")

def factorial2(n):
    i = 1
    result = 1

    if n < 0:
        print("Factorial is not findable for this number!")
    else:
        while i <= n:
            result *= i
            i += 1
        print("Factorial is : ", result)
        

