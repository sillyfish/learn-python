"""
Title: 
Date: 2023-05-15 12:20:06
LastEditTime: 2023-05-15 12:20:07
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""

from pathlib import Path


files = ["cats.txt", "dogs.txt"]
for file in files:
    path = Path(file)
    try:
        content = path.read_text()
        print(content)
    except FileNotFoundError:
        # print(f"File {file} not found!")
        pass
