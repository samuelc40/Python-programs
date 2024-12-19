# example of a user defined function

def sample(num1,num2):
    sum = num1 + num2
    return sum
result = sample(int(input("Enter the Number 1: ")),int(input("Enter the Number 2: ")))
print(result)

# Sorting using lambda function by the length of the names

name = ["Alan","Soloman","Samuel","Edwin","Sharon","Augustine"]
name.sort(key  = lambda x:len(x))
print(name)