# var = open("new_file.txt","r")
# var = open("C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/new_file.txt", "r")

# print(var.read())

# var.close()

# Modes in file handling are : 'r' for read and 'w' for write, 'a' for append, 'x' for creating.

# var = open("C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/new_file.txt", "w")

# var.write(' The open command will open the Python file in the read mode and the for loop will print each line present in the file.')

# print(var.read())

# create_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt', 'w')

# create_var.write('Hello world! \n')

# create_var.write('Hello, this is Arcraft infotech\nWe are glad to hire you')

# create_var.close()

# append_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt', 'a')

# append_var.write('\nThis is for checking if the append mode is working or not...')

# append_var.close()

# read_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt', 'r')

# print(read_var.read())

# read_var.close()

# readline_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/dict2.py', 'r')

# print(readline_var.read())
# # print(readline_var.readline(4))

# readline_var.close()

# writeline_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt', 'a')

# writeline_var.writelines(['\nTying to add new sentence using write lines in write mode'])

# writeline_var.close()

# readwrite_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt', 'r')

# print(readwrite_var.read())

# readable_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt', 'r')

# print(readable_var.readable())
# print(readable_var.writable())

# import os

# os.remove('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/write_file.txt')

# readable_var = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/dict2.py', 'r+')
# readable_var2 = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/multi_table.py', 'a')

# content = readable_var.read()
# print(content)
# readable_var2.write(content)
# print(readable_var2.read())

# readable_var.close()
# readable_var2.close()

# read_file = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/text_file.txt', 'r', encoding='utf-8')
# content = read_file.read()

# print(content)
# read_file.close()

# write_file = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/text_file.txt', 'w', encoding='utf-8')
# write_file.writelines(['Here, we have overridden the constructor of the Exception class to accept our own custom \n', 'arguments salary and message.\n', 'Then, the constructor of the parent Exception class is called manually with the self.message argument using super().\n'])

# # print(content)
# write_file.close()

# read_file = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/text_file.txt', 'r', encoding='utf-8')
# content = read_file.read()

# print(content)

# read_file.close()

# writable_file = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/text_file.txt', 'w', encoding='utf-8')
# writable_file.write('Then, the constructor of the parent Exception class is called manually with the self.message argum')
# print(writable_file.writable())

read_file = open('C:/Users/Samuel Joseph/Desktop/New folder/PycharmProjects/Anjali miss tasks/text_file.txt', 'r', encoding='utf-8')

content_list = read_file.readlines()

print(len(content_list))
