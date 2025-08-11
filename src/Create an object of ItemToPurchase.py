# Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")

    def get_total_cost(self):
        return self.item_price * self.item_quantity

# Main section
print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

# Print total cost for each item
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

# Calculate and display total
total = item1.get_total_cost() + item2.get_total_cost()
print(f"\nTotal: ${int(total)}")




