"""
Title: 
Date: 2023-05-13 17:26:55
LastEditTime: 2023-05-13 17:26:55
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
from pathlib import Path


guest_string = ""
name = ""
while name != "q":
    name = input("Please input your name: ")
    if name != "q":
        guest_string += name + "\n"

path = Path("guest_book.txt")
path.write_text(guest_string)
