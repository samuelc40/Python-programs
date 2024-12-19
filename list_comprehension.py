# Write a list comprehension that returns the list '["1*2 = 2", "2*2 = 4", "3*2 = 9,....., "25*2 = 625"]'

result = [f"{i}*2 = {i*i}" for i in range(1,26)]
print(result)