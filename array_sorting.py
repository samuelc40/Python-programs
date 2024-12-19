arr2=[]
size=int(input("Enter the size: "))
print("Enter the values of the array: ")
for i in range(0, size):
    values=int(input())
    arr2.append(values)

print("The array is: ",arr2)

temp=0
for i in range(0, len(arr2)):
    for j in range(i+1, len(arr2)):
        if arr2[i] > arr2[j]:
            temp = arr2[i]
            arr2[i] = arr2[j]
            arr2[j] = temp

print("The sorted array is: ",arr2)


