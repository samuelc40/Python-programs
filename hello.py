mark1 = int(input("Enter your marks kid : "))
mark2 = int(input())
mark3 = int(input())
sum = mark1 + mark2 + mark3
print(sum)
mark = sum/3
print("Average is : " + str(mark))
if mark<=100 and mark>90:
    print("A plus")
elif mark <= 89 and mark >= 80:
    print("A only")
elif mark <= 79 and mark >= 70:
    print("B plus")
elif mark <= 69 and mark >= 60:
    print("B grade")
elif mark <= 59 and mark >= 50:
    print("C plus")
elif mark <= 49 and mark >= 40:
    print("C grade")
elif mark <= 39 and mark >= 0:
    print("Failed...!!!")
else:
    print("Wrong entry!")




