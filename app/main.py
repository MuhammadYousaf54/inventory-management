# app/main.py

from auth import Auth
from inventory import Inventory
from models import Product
from utils import display_message

def start():
    auth = Auth()
    user = auth.login()
    if not user:
        return

    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1" and auth.authorize(user, "admin"):
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))
            product = Product(product_id, name, category, price, stock_quantity)
            inventory.add_product(product)

        elif choice == "2" and auth.authorize(user, "admin"):
            product_id = input("Enter Product ID to update: ")
            name = input("Enter new Product Name (leave blank to skip): ")
            category = input("Enter new Product Category (leave blank to skip): ")
            price = input("Enter new Product Price (leave blank to skip): ")
            stock_quantity = input("Enter new Stock Quantity (leave blank to skip): ")

            update_data = {}
            if name: update_data["name"] = name
            if category: update_data["category"] = category
            if price: update_data["price"] = float(price)
            if stock_quantity: update_data["stock_quantity"] = int(stock_quantity)

            inventory.update_product(product_id, **update_data)

        elif choice == "3" and auth.authorize(user, "admin"):
            product_id = input("Enter Product ID to delete: ")
            inventory.delete_product(product_id)

        elif choice == "4":
            inventory.view_inventory()

        elif choice == "5":
            display_message("Exiting Inventory Management System.")
            break

        else:
            display_message("Invalid option or unauthorized access.")

if __name__ == "__main__":
    start()
