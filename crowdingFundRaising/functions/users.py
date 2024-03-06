import re
import json
from functions.helper import is_string

class Auth:

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                users_data = json.load(file)
                return users_data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def save_users(self,users):
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

    def signup(self):
        # Patterns
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        mobile_pattern = r'^\+20\d{11}$'

        # Empty and patterns validations
        first_name = input("Enter first name: ")
        while not is_string(first_name.strip()):
            first_name = input("Required! Enter first name: ")

        last_name = input("Enter last name: ")
        while not is_string(last_name.strip()):
            last_name = input("Required! Enter last name: ")

        email = input("Enter email: ")
        while not re.match(email_pattern, email):
            print("Invalid email format. Please enter a valid email.")
            email = input("Enter email: ")

        password = input("Enter password: ")
        while not password:
            password = input("Required! Enter password: ")

        confirm_password = input("Confirm password: ")
        while password != confirm_password:
            print("Passwords do not match. Please try again.")
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")

        mobile_phone = input("Enter mobile phone number: ")
        while not re.match(mobile_pattern, mobile_phone):
            print("Invalid phone number format. Please enter a valid Egyptian phone number.")
            mobile_phone = input("Enter mobile phone number: ")

        # Create new user
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "mobile_phone": mobile_phone
        }

        # Load existing users
        users = self.load_users()

        # Add new user to the list
        users.append(user_data)

        # Save updated user list
        self.save_users(users)

        print("User signed up successfully!")        

    def login(self):
        # Empty validation
        email = input("Enter email: ")
        while not email:
            email = input("Required! Enter email: ")

        password = input("Enter password: ")
        while not password:
            password = input("Required! Enter password: ")

        # Find user
        with open("users.json", 'r') as file:
            data = json.load(file)
            found_user = None
            for user in data:
                if email == user['email'] and password == user['password']:
                    found_user = user
                    break

            if found_user:
                return found_user
            else:
                print("Invalid email or password.")
                return None

    def logout(self):
        print("Logged out successfully.")


