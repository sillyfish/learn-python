"""
Title: 
Date: 2023-05-13 16:47:31
LastEditTime: 2023-05-13 17:01:47
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
from pathlib import Path


path = Path("learning_python.txt")
content = path.read_text()
print(content)

# lines = content.splitlines()
learn_string = ""
for line in content.splitlines():
    learn_string += line

print(learn_string)
