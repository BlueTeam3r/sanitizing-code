#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

def main():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    api_key=os.getenv("API_KEY")
    print("We are up and running!")
    print(f"The username is {username}\nThe password is {password}\nThe api key is {api_key}")

if __name__ == "__main__":
    main()