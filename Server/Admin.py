import json
from encryption import hash
import os

def Admin(conn, name):
    if name == 'Admin': #If you want to change the admin name change this
        with open('info.json') as pwd_file:
            data = json.load(pwd_file)
            input_password = input("password -> ")
            hash_pwd = hash(input_password)
            password = data["password"]
            if password == hash_pwd:
                print("you just logge in ")


Admin(" ", "Admin")