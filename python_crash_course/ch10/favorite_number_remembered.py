"""
Title: 
Date: 2023-05-15 16:23:52
LastEditTime: 2023-05-15 16:23:52
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""

import json
from pathlib import Path


path = Path("favorite_number.json")
if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number! It's {number}.")
else:
    number = input("Please input your favorite number: ")
    contents = json.dumpm(number)
    path.write_text(contents)
    print("I will remember your favorite number!")
