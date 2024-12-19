# A lambda funcntion is a small anonimous function that can take any number of arguments

# lambda arguments : function expression

x = lambda a : a + 10

print(x(3))

# ------------------------------------------------------------------------------------------------------------------------

y = lambda a, b, c : a * (b + c)

print(y(2, 3, 4))

# ------------------------------------------------------------------------------------------------------------------------

my_list = [1, 2, 3, 4, 5, 6]

var = map(lambda p : p ** 2, my_list)

print(list(var))

# ------------------------------------------------------------------------------------------------------------------------

var2 = filter(lambda p : p % 2 == 0, my_list)

print(list(var2))

# ------------------------------------------------------------------------------------------------------------------------

# char_list = ['apple', 'orange', 'pineapple', 'avocado', 'banana', 'grapes', 'watermelon']

# vowels = ['a', 'e', 'i', 'o', 'u'] 

# var3 = filter(lambda p : p[0] in vowels, char_list) 

# # print(list(var3))

# map_var = map(lambda p : capitalize(p), list(var3))

