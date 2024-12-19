
# Problem 2

class Restaurant:
    
    def __init__(self):
        # self.menu_items = ['Veg noodled', 'Chicken noodle', 'Schezwan chicken noodles', 'Mixed noodles', 'Veg soup', 'Chicken soup', 'Veg fried rice', 'Chicken fried rice', 'Chilly chicken', 'Chilly gopi', 'chilly Paneer']
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def display_menu(self):
        for item_name, price in self.menu_items.items():
            print(f"{item_name} - ${price}")

    def add_items_to_menu(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"Added {item_name} with price {price} to the menu. ")

    def book_tables(self, table_number, customer_name):

        self.book_table.append({
            'table_number': table_number, 
            'customer_name': customer_name
            })
        
        print(f"Table {table_number} has been booked for {customer_name}.")

    def customer_order(self, table_number, ordered_items):
        order = {"table_number": table_number, "items": ordered_items}
        self.customer_orders.append(order)
        print(f"Order for table {table_number}: {ordered_items}")

    def print_table_reservations(self):
        for reservation in self.book_table:
            print(f"Table {reservation['table_number']} is reserved for {reservation['customer_name']}")

    def print_customer_orders(self):
        print("Customer Orders: ")
        for orders in self.customer_orders:
            print(f"Table {orders['table_number']} ordered {orders['items']}.")




my_restaurant = Restaurant()

my_restaurant.add_items_to_menu("Veg noodles", 12.99)
my_restaurant.display_menu()
my_restaurant.book_tables(1, "Samuel")
my_restaurant.customer_order(1, ["veg noodles", "Chicken noodles"])
my_restaurant.print_table_reservations()
my_restaurant.print_customer_orders()


















#     def get_menu_items(self):
#         i = 1
#         for item in self.menu_items:
#             print(f'{i}. {item}')
#             i += 1

#     def add_menu_item(self):
#         print("Enter the items to add for todays menu or press q to back: ")
#         while True:
#             new_items = input()

#             if new_items == 'q' or new_items == 'Q':
#                 print('You quit!')
#                 break

#             else:
#                 self.menu_items.append(new_items)

#     def reserve_table(self):
#         print("Available tables are 1 to 6.")
#         table_num = int(input('Enter table number you want to reserve: '))
#         # if table_num in 
#         if table_num in self.reserved_tables:
#             print("Sorry, Table is already reserved...!")

#         elif table_num > 0 and table_num <= 6:
#             self.table_no = table_num

#         else:
#             print("Selected table is not available! or Wrong entry!")



# obj1 = Restaurant('Samuel')

# # obj1.get_menu_items()

# # obj1.add_menu_item()

# obj1.get_menu_items()

# obj1.reserve_table()

