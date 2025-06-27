import json
from models import user
from db.database import load_data, save_data

def register():
    data = load_data()
    username = input("Enter username: ")
    password = input("Enter password: ")

    for u in data['users']:
        if u['username'] == username:
            print("Username already exists.")
            return

    phone = input("Enter phone number: ")   
    new_user = user.create_user(username, password, phone)
    data['users'].append(new_user)
    save_data(data)
    print("User registered successfully.")

def login():
    data = load_data()
    username = input("Enter username: ")
    password = input("Enter password: ")

    for u in data['users']:
        if u['username'] == username and u['password'] == password:
            print("Login successful.")
            return u
    print("Invalid Username or Password.")
    return None
