# Write a function to calculate the sum of all numbers passed as its arguments. Your function should be called sum_numbers
# and should define a single variable argument (i.e. a star argument) that will get the values to sum.


def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1.1,2.2,5.5)
print("Result: ",result)