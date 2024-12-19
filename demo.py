# n = 3
# for i in range(1, n):
#     for j in range(1, i * i):
#         print("* ", end=" ")
#         if( j % ( i * 2 ) == 0):
#             print("\n", end=" ")
#     if (i==n):
#         break
#     for k in range(1, n):
#         print("* ", end=" ")
#     print("\n", end=" ")


# ---------------------------------------------------------------------------------------------------------------------



# target = 10
# arr = []
# arr1 = []
# size = int(input("Enter the size of your array: "))
# print("Enter the values in your array: ")
# for i in range(0, size):
#     values = int(input())
#     arr.append(values)
# # print(arr, end=" ")
# print("\n", end=" ")

# def task():
#     for i in range(0, len(arr)-1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 arr1.append((arr[i], arr[j]))
# task()
# print(arr1)


# --------------------------------------------------------------------------------------------------------------------------------
        

# choice = int(input("How do you want your array? press one for assending, 2 for desending: "))
# if choice == 1:
#     for i in range(0, len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     print("Your array is: ", arr)
# elif choice == 2:
#     for i in range(0, len(arr) - 1):
#         for j in range(i + 1, len(arr)):
#             if arr[i] < arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     print("Your array is: ", arr)
# else: 
#     print("Invalid Entry, Try to use sense next time!!!")


# --------------------------------------------------------------------------------------------------------------------------------

# class TwoDArray:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.array1 = []
#         self.array2 = []
#         self.resultarray = []

#     def GetArray(self):
#         print("Enter the values in the first array: ", )
#         for i in range(self.rows):
#             a = []
#             for j in range(self.cols):
#                 a.append(int(input()))
#             self.array1.append(a)
#         print("The frist array is: ")
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.array1[i][j], end=" ")
#             print()

#         print("Enter the values in the second array: ", )
#         for i in range(self.rows):
#             b = []
#             for j in range(self.cols):
#                 b.append(int(input()))
#             self.array2.append(b)
#         print("The second array is: ")
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.array2[i][j], end=" ")
#             print()

#     def AddArray(self):
#         for i in range(self.rows):
#             c = []
#             for j in range(self.cols):
#                 c.append(self.array1[i][j] + self.array2[i][j])
#             self.resultarray.append(c)
        
#     def DisplayArray(self):
#         print("Addition your both arrays is: ")
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.resultarray[i][j], end=" ")
#             print()


# obj = TwoDArray(3, 3)
# obj.GetArray()
# obj.AddArray()
# obj.DisplayArray()

# ----------------------------------------------------------------------------------------------------------------------------------------

# def PttrnPrnt(n):
#     for i in range(1, 2*n+1):
#         if i <= n:
#             new_i = i
#         else:
#             new_i = 2*n - i
#         for j in range(new_i):
#             print(j, end=" ")
#         print()
           

# n = int(input("Enter the number of size for you pattern: "))

# PttrnPrnt(n)

# target = 10
# n = int(input("Enter the size of your array: "))
# a=[]
# resultarray = []
# print("Enter the values in your array: ")
# for i in range(n):
#     value = int(input())
#     a.append(value)
# print()
# print("Your array is: ")
# for i in a:
#     print(i, end=" ")
# print("\n")
# print("Sorted order of this array is: ")
# for i in range(0, len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] == target:
#             resultarray.append((a[i], a[j]))

# for i in resultarray:
#     print(i, end=" ")

# class ArraySorting:
#     def __init__(self,rows,cols):
#         self

# num1 = int(input("Enter the 2 numbers: "))
# num2 = int(input())

# def add():
#     sum = num1 + num2
#     print(sum)

# def sub():
#     sub = num1 - num2
#     return sub

# def mul(a, b):
#     print(a, b)
#     ans = a * b
#     print(ans)

# def div(a, b):
#     ans = a / b
#     return ans

# choice = int(input("Enter a choice for operation / 1 - Addiition, 2 - Substraction, 3 - Multiplication, 4 - Division: "))

# if choice == 1:
#     print("Selected addition, Your answer is: ", add())
# elif choice == 2:
#     print("Selected substraction, Your answer is: ", sub())
# elif choice == 3:
#     print("Selected multiplication, Your answer is: ", mul(num1, num2))
# elif choice == 4:
#     print("Selected division, Your answer is: ", div(num1, num2))
# else:
#     print("Invalid option!")


# size = int(input("Enter the size of the array: "))


# ----------------------------------------------------------------------------------------------------------------------------------------


# class TwoDArray:
#     def __init__(self ,rows ,cols):
#         self.rows = rows
#         self.cols = cols
#         self.Array1 = []
#         self.Array2 = []
#         self.ResultArray = []

#     def getArray(self):
#         print("Enter the values in the first array: ")
        
#         for i in range(self.rows):
#             a = []
#             for j in range(self.cols):
#                 a.append(int(input()))
#             self.Array1.append(a)
#         print("First array is:")

#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.Array1[i][j], end = " ")
#             print()

#         print(" Enter the second array: ")

#         for i in range(self.rows):
#             b = []
#             for j in range(self.cols):
#                 b.append(int(input()))
#             self.Array2.append(b)
#         print("Second Array is: ")

#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.Array2[i][j], end = " ")
#             print()

#     def addArray(self):
#         for i in range(self.rows):
#             c = []
#             for j in range(self.cols):
#                 c.append(self.Array1[i][j] + self.Array2[i][j])
#             self.ResultArray.append(c)

#     def printArray(self):
#         print("Result array is: ")
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 print(self.ResultArray[i][j], end = " ")
#             print()

# obj = TwoDArray(3, 3)
# obj.getArray()
# obj.addArray()
# obj.printArray()

# ----------------------------------------------------------------------------------------------------------------------------------------


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("Head is None")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "--->",end = " ")
#                 n = n.ref

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_node

#     def add_after(self, data, x):
#         n = self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n = n.ref
#         if n is None:
#             print("Enter node is not present in the linked list!")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node


# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_begin(30)
# LL1.add_end(100)
# LL1.add_end(200)
# LL1.add_after(25, 20)
# LL1.print_LL()


# ----------------------------------------------------------------------------------------------------------------------------------------


