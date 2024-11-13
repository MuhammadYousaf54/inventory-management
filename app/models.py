# app/models.py

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return (f"Product({self.product_id}, {self.name}, {self.category}, "
                f"{self.price}, {self.stock_quantity})")

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password  # In production, use a hash function to store passwords securely
        self.role = role  # 'admin' or 'user'

    def __repr__(self):
        return f"User({self.username}, {self.role})"

    def check_password(self, password):
        return self.password == password
