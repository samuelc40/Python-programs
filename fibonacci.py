
n = int(input("Enter the limit of the pattern: "))

fib1 = 0
fib2 = 1
i = 1
print(fib1, end=" ")
print(fib2, end=" ")
while i < n - 1:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print(fib, end=" ")
    i += 1


