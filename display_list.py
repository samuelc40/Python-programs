
n = int(input("Enter the length of the list: "))

list = []

for i in range(1, n+1):
    list.append(input(f"Enter the value {i}: "))
    print(" ")
print("The list is : ", list)

print("And the values are : ")

for i in list:
    print(i, end="\t")