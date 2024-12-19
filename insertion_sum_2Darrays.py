A = []
n = int(input("Enter the N for N x N matrix: "))
print("Enter the values")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

print("First Array is : ",A)

for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
    print()

B = []

n = int(input("Enter the N for N x N Array: "))
print("Enter the values: ")

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)
print("Second Array is: ",B)

for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ")
    print()

print("Result is: ")

result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

for r in result:
    print(r)



