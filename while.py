from Module import CheckNegOrNot as A
A(int(input("Enter Your Number : ")))

n=(int(input("Enter another number for another Program : ")))
for i in range(n+2):
    for j in range(1,i):
        print(j,end=" ")

    print('')