# app/auth.py

from models import User
from utils import raise_error

class Auth:
    def __init__(self):
        # Mocked user database (in a real system, replace with a database or JSON file)
        self.users = {
            "admin": User("admin", "admin123", "admin"),
            "user": User("user", "user123", "user")
        }

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.users.get(username)

        if user and user.check_password(password):
            print(f"Login successful! Role: {user.role}")
            return user
        else:
            raise_error("Invalid credentials.")
            return None

    def authorize(self, user, required_role):
        if user.role == required_role:
            return True
        else:
            raise_error("Unauthorized action.")
            return False
