
# read_file = open("C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/multiplication_table.py", "r")
# write_file = open("C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/multi_table.py", "w")

# # print()
# print(read_file.read())
# content = read_file.read()

# write_file.write(content)

# read_file.close()
# write_file.close()

read_file = open("C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/multiplication_table.py", "r")

# Open the destination file in write mode
write_file = open("C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/multi_table.py", "w")

# Read the content of the source file and print it
content = read_file.read()
print(content)

# Write the content to the destination file
write_file.write(content)

# Close both files
read_file.close()
write_file.close()