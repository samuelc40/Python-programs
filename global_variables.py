def main():
    global A,n
    n = int(input("Enter the size of the array: "))
    A = []
    get_array()
    dis_array()
def get_array():
    print("Enter the values of Array: ")
    for i in range(0,n):
        values = int(input())
        A.append(values)
def dis_array():
    for i in range(n):
        print(A[i],end=" ")

main()
