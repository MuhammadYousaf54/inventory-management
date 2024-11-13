# app/inventory.py

from models import Product
from utils import raise_error, display_message
import json
import os

class Inventory:
    DATA_FILE = "data/inventory.json"

    def __init__(self):
        self.load_inventory()

    def load_inventory(self):
        # Load inventory data from JSON file
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                self.products = [Product(**data) for data in json.load(file)]
        else:
            self.products = []

    def save_inventory(self):
        # Save inventory data to JSON file
        with open(self.DATA_FILE, "w") as file:
            json.dump([product.__dict__ for product in self.products], file)

    def add_product(self, product):
        self.products.append(product)
        display_message(f"Product '{product.name}' added successfully.")
        self.save_inventory()

    def update_product(self, product_id, **kwargs):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            display_message(f"Product '{product_id}' updated successfully.")
            self.save_inventory()
        else:
            raise_error("Product not found.")

    def delete_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]
        display_message(f"Product '{product_id}' deleted successfully.")
        self.save_inventory()

    def view_inventory(self):
        for product in self.products:
            print(product)
