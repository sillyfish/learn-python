"""
Title: 
Date: 2023-05-15 16:40:04
LastEditTime: 2023-05-15 16:40:04
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""

import json
from pathlib import Path


def get_new_user(path):
    """Prompt for a new user"""
    user = {}
    user["name"] = input("Please input your name: ")
    user["age"] = input("Please input your age: ")
    user["favorite_number"] = input("Please input your favorite number: ")
    path.write_text(json.dumps(user))


def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        return json.loads(path.read_text())
    return None


def greet_user():
    """Greet the user by name."""
    path = Path("user.json")
    user = get_stored_user(path)
    if user:
        is_user = input(f"Is your name {user['name']}? (y/n) ")
        if is_user == "y":
            print(f"Welcome back, {user['name']}!")
            return

    get_new_user(path)
    print("We'll remember you when you come back!")


greet_user()
