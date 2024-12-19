# Write a program to print HELLO WORLD using function without using print inside of the function ("HELLO WORLD " must be inside the decorator fuction)

# Note : A decorator is a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a fuction want to decorate.

def decorator_function(func):
    def wrapper():
        message = "HELLO WORLD"
        return func(message)
    return wrapper()
@decorator_function
def my_function(message):
    return message
print(my_function)


# Or the simple and non complicated method is without wrapper method

print("Second method")

def decorator_function(func):
    func = "HELLO WORLD"
    return func
@decorator_function
def my_function(A):
    return A
print(my_function)



