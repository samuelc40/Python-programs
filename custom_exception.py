# create a custom exception class and raise this exception when user press one in the menu
# and handles this excption


# Defining custom exception class
class InvalidMenuOptionException(Exception):
    pass

def display_menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

def get_user_menu():
    choice = input("Enter your option: ")
    if choice not in ["1", "2", "3"]:
        raise InvalidMenuOptionException("Invalid menu option selected!")
    return choice

try:
    display_menu()
    user_choice = get_user_menu()
    print("User selected option ",user_choice)
except InvalidMenuOptionException as e:
    print(e)

# Another method is given below

class InvalidMenuOptionException(Exception):
    pass

def menu():
    choice = input("Enter you choice from one to 4: ")
    if choice == "1":
        raise InvalidMenuOptionException("Option one is currently not working !")
    elif choice == "2":
        print("You have selected Option 2")
    elif choice == "3":
        print("You have selected Option 3")
    elif choice == "4":
        print("You have selected Option 4")
    else:
        print("Invalid selection!")

try:
    menu()
except InvalidMenuOptionException as e:
    print("Error: ",e)