import json
import os

def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    for product in inventory:
        print("ID:", product["id"], "| Name:", product["name"], 
              "| Price: $" + str(product["price"]), "| Stock:", product["stock"])
    print("------------------------------------------------")


def search_product(inventory):
    search_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == search_id:
            print("Product Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price: $" + str(product["price"]))
            print("Stock:", product["stock"])
            print("------------------------------------------------")
            return
    print("Product not found.")


def add_product(inventory):
    new_id = input("Product ID: ")
    new_name = input("Product Name: ")
    new_price = float(input("Price: "))
    new_stock = int(input("Stock Quantity: "))
    
    new_product = {"id": new_id, "name": new_name, "price": new_price, "stock": new_stock}
    inventory.append(new_product)
    print("Product added successfully!")
    return inventory




def update_stock(inventory):
    search_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == search_id:
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])
            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock
            print("Stock updated successfully!")
            return
    print("Product not found.")


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully to inventory.json.")


def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            data = json.load(file)
        print("Inventory loaded successfully.")
        return data
    else:
        print("No inventory.json found. Starting with empty inventory.")
        return []


# ---- Main program starts here ----
# ---- Main program starts here ----
print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)

inventory = load_inventory()

while True:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    choice = input("Enter option: ")

    if choice == "1":
        display_all(inventory)
    elif choice == "2":
        inventory = add_product(inventory)
    elif choice == "3":
        update_stock(inventory)
    elif choice == "4":
        search_product(inventory)
    elif choice == "5":
        save_inventory(inventory)
    elif choice == "6":
        save_inventory(inventory)
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
    