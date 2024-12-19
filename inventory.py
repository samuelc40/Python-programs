
# Problem 4

class Inventory:
    def __init__(self):
        self.items = {}
        self.current_id = 0
        # self.item_id = {}
        # self.item_name = []
        # self.stock_count = None
        # self.price = None

    def add_item(self, item_name, item_count, price):
        self.current_id += 1
        self.items[self.current_id] = {
            'name': item_name,
            'stock': item_count,
            'price': price,
            }
        print("New item added to inventory:",item_name, ",\nstock count:", item_count, "\nprice : ", price)
        print("")

    def update_item(self, item_id, item_name=None, item_count=None, price=None):
        if item_id in self.items:
            if item_name is not None:
                self.items[item_id]['name'] = item_name
            if item_count is not None:
                self.items[item_id]['stock'] = item_count
            if price is not None:
                self.items[item_id]['price'] = price
        else:
            print(f"Item ID - {item_id} is not found in the invetory!")
            print("")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty!")
            print("") 
        else:
            print("Current inventory: ")
            for item_id, details in self.items.items():
                print(f"Item ID: {item_id},\nName: {details['name']}, \nStock: {details['stock']}, \nPrice: {details['price']}")
                print("")

item1 = Inventory()
item1.add_item("Keyboard", 4, 5000)
item1.update_item(item_id=1, item_name="guitar", item_count=8, price=None)
item1.add_item("keyboard", 4, 7599)
item1.display_inventory()