b=int(input("Enter a : "))
f=int(input("Enter b : "))

try:
    a=f/b
    print(a)
    print("Try completed")
except ZeroDivisionError:
    print("Can't divided by zero")
print("Program completed")


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


c=int(input("Enter c: "))
d=int(input("Enter d: "))

try:
    e=c/d
    print(e)
    print("Second Try completed")

except ZeroDivisionError:
    print("Syntax Error !!!! Cant be divided by Zero...")
print("Program Exited")


