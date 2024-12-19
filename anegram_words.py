
my_string = 'ate'

my_string2 = 'eat'


my_string_to_list = list(my_string)

my_string2_to_list = list(my_string2)

my_set = set(my_string_to_list)

my_list = list(my_set)

# sorted = my_list.sort()

# if my_string_to_list.sort() == sorted:
#     if my_string2_to_list.sort() == sorted:
#         print("Both the words are anegram...")

# else:
#     print("Not anegram...")

if sorted(my_string) == sorted(my_string2):
    print("Both are anegram...")
else:
    print("Not anegram...")