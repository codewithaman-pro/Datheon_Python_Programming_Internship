class InventoryItem:
    """Represents an individual item in the inventory."""
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id} | Name: {self.name} | Qty: {self.quantity} | Price: ₹{self.price:.2f}"


class Inventory:
    """Manages a collection of InventoryItems, implementing custom Iterator behavior."""
    def __init__(self):
        self.items = {}  # Dictionary to store items by item_id

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            self.items[item_id].quantity += quantity
            print(f"Updated existing item: {name} (New Qty: {self.items[item_id].quantity})")
        else:
            self.items[item_id] = InventoryItem(item_id, name, quantity, price)
            print(f"Added new item: {name}")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed = self.items.pop(item_id)
            print(f"Removed item: {removed.name}")
        else:
            print("Error: Item ID not found in inventory.")

    def display_inventory(self):
        print("\n--- Current Inventory Status ---")
        if not self.items:
            print("Inventory is empty.")
        for item in self:
            print(item)
        print("--------------------------------\n")

    # Implementing Iterator pattern as shown in Python docs (Section 9.9)
    def __iter__(self):
        self._index = 0
        self._item_keys = list(self.items.keys())
        return self

    def __next__(self):
        if self._index < len(self._item_keys):
            key = self._item_keys[self._index]
            self._index += 1
            return self.items[key]
        else:
            raise StopIteration


def main():
    my_inventory = Inventory()
    
    while True:
        print("==============================")
        print("     OOP INVENTORY SYSTEM     ")
        print("==============================")
        print("1. Add / Update Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            try:
                item_id = input("Enter Item ID: ").strip()
                name = input("Enter Item Name: ").strip()
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price per unit: "))
                my_inventory.add_item(item_id, name, quantity, price)
            except ValueError:
                print("Invalid input! Please enter correct numbers for quantity and price.")
                
        elif choice == '2':
            item_id = input("Enter Item ID to remove: ").strip()
            my_inventory.remove_item(item_id)
            
        elif choice == '3':
            my_inventory.display_inventory()
            
        elif choice == '4':
            print("Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 to 4.")

if __name__ == "__main__":
    main()