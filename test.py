class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    # Method to add items to the menu
    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"Added {item_name} with price {price} to the menu.")

    # Method to book a table
    def book_tables(self, table_number, customer_name):
        self.book_table.append({"table_number": table_number, "customer_name": customer_name})
        print(f"Table {table_number} has been booked for {customer_name}.")

    # Method to take customer orders
    def customer_order(self, table_number, ordered_items):
        order = {"table_number": table_number, "items": ordered_items}
        self.customer_orders.append(order)
        print(f"Order for table {table_number}: {ordered_items} has been placed.")

    # Method to print the menu
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    # Method to print table reservations
    def print_table_reservations(self):
        print("Table Reservations:")
        for reservation in self.book_table:
            print(f"Table {reservation['table_number']} is reserved for {reservation['customer_name']}.")

    # Method to print customer orders
    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']} ordered {order['items']}.")

# Creating an instance of Restaurant
my_restaurant = Restaurant()

# Adding items to the menu
my_restaurant.add_item_to_menu("Pizza", 12.99)
my_restaurant.add_item_to_menu("Burger", 9.99)
my_restaurant.add_item_to_menu("Pasta", 10.99)

# Making table reservations
my_restaurant.book_tables(1, "John Doe")
my_restaurant.book_tables(2, "Jane Smith")

# Taking customer orders
my_restaurant.customer_order(1, ["Pizza", "Pasta"])
my_restaurant.customer_order(2, ["Burger"])

# Printing the menu
my_restaurant.print_menu()

# Printing table reservations
my_restaurant.print_table_reservations()

# Printing customer orders
my_restaurant.print_customer_orders()
