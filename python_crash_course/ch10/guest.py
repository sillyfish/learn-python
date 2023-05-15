"""
Title: 
Date: 2023-05-13 17:24:27
LastEditTime: 2023-05-13 17:24:28
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
from pathlib import Path


name = input("Please input your name: ")
path = Path("guest.txt")
path.write_text(name)
