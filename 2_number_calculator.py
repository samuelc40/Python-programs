num1 = int(input("Enter 2 Numbers: "))
num2 = int(input())

#without argument without return value
def add():
    sum = num1 + num2
    print(sum)

# without argument with return value
def sub():
    a = num1
    b = num2
    res = a - b
    return res

# with argument without return value
def multi(a,b):
    res = a * b
    print(res)

# with argument with return value
def div(a,b):
    res = a / b
    return res

choice = int(input("Enter 1 for addition / Enter 2 for substraction / Enter 3 for multipliaction / Enter 4 for division: "))

if choice == 1:
    print("You have chosen addition, Your requested Result is: ",add())
elif choice == 2:
    print("You have chosen Substraction, Your requested Result is: ",sub())
elif choice == 3:
    print("You have chosen Multiplication, Your requested Result is: ",multi(num1,num2))
elif choice ==4:
    print("You have chosen Division, Your requested Result is: ",div(num1,num2))
else:
    print("Please select a valid option next time!!!")
