
import math

def find_square_root(x):
    if x < 0:
        return "Cannot find the square root of a negative number! "
    else:
        return math.sqrt(x)
    
number = float(input("Enter the number: "))
result = find_square_root(number)

print(f"Square root of the given number is: {result}")