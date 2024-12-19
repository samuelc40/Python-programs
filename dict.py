
# my_dict = {
#     {'name': 'Samuel', 'age': 22},
#     {'name': 'joel', 'age': 23},
#     {'name': 'anjali', 'age': 27},
# }

# print(my_dict)

my_dict1 = {
    'name': 'Samuel',
    'age': 22,
    'name2': 'sharon',
    'age2': 20,
}

my_dict2 = {
    'name': 'joel',
    'age': 23
}

my_dict3 = {
    'name': 'anjali',
    'age': 27
}

my_dict = {
    'dict1': my_dict1,
    'dict2': my_dict2,
    'dict3': my_dict3
}

print(my_dict)

my_dict.update({'course': 'Data science'})

my_dict2.update({'name': 'soloman'})

print(my_dict2)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# my_dict.pop('dict1')
# my_dict.clear()
print(my_dict)

my_dict1.pop('name2')

print(my_dict)

