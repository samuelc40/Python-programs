class TwoDArray:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.array1 = []
        self.array2 = []
        self.resultArray = []

    def GetArray(self):
        print("Enter the values in the first array: ")
        for i in range(self.rows):
            a = []
            for j in range(self.columns):
                a.append(int(input()))
            self.array1.append(a)
        print("First Array is : ")
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.array1[i][j], end=" ")
            print()

        print("Enter the values in the second array: ")
        for i in range(self.rows):
            b = []
            for j in range(self.columns):
                b.append(int(input()))
            self.array2.append(b)
        print("Second Array is : ")
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.array2[i][j], end=" ")
            print()
    def addArray(self):
        for i in range(self.rows):
            c = []
            for j in range(self.columns):
                c.append(self.array1[i][j] + self.array2[i][j])
            self.resultArray.append(c)

    def displayArray(self):
       print("Result is : ")
       for i in range(self.rows):
           for j in range(self.columns):
               print(self.resultArray[i][j], end=" ")
           print()

obj = TwoDArray(3, 3)
obj.GetArray()
obj.addArray()
obj.displayArray()


