from functools import reduce

num_list = [1, 2, 3, 4, 10, 5, 6, 7, 8, 9]

var = reduce(lambda x, y : x + y, num_list)

print(var)

var2 = reduce(lambda x, y : x if x > y else y, num_list)

# var2 = lambda x, y : x if x > y else y

print(var2)

# --------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to find the sum of squares of all even numbers in a list using map, filter, and reduce.

fil_var = filter(lambda x : x % 2 == 0 , num_list)

map_var = map(lambda x : x ** 2, list(fil_var))

red_var = reduce(lambda x, y : x + y, list(map_var))

print(red_var)

# --------------------------------------------------------------------------------------------------------------------------------

char_list = ['apple', 'orange', 'pineapple', 'avocado', 'banana', 'grapes', 'watermelon']

vowels = ['a', 'e', 'i', 'o', 'u'] 

var3 = filter(lambda p : p[0] in vowels, char_list) 

# print(list(var3))

map_var = map(lambda p : p.capitalize(), list(var3))

print(list(map_var))