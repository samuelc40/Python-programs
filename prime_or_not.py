
val = int(input("Enter the value to check prime or not: "))

if val * 1 == val and val/val == 1 and val % 2 == 1 and val % 3 is not None:
    if val == 1:
        print("One is not a prime number!")
    else:
        print(f"Your entered value {val} is a prime number")
else:
    print(f"Your entered value {val} is not a prime number")

