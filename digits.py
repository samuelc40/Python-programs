
try:
    num = int(input("Enter a number to find the number number of digits : "))
    
except ValueError:
    print("Please enter a valid number!!!")
    num = None

if num is not None:
    digits = str(num)
    print("The number of digits in the given number is : ", len(digits))
    
else:
    print("Program stopped because of ValueError Exception!")



