"""
Title: 
Date: 2023-04-20 15:17:58
LastEditTime: 2023-04-20 16:15:00
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-20 15:17:58
LastEditTime: 2023-04-20 15:18:00
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
glossary = {
    "list": "a list of things",
    "tuple": "a tuple of things",
    "dictionary": "a dictionary of things",
    "if": "if something is true",
    "for": "for something in something",
}

print(glossary)

glossary = {
    **glossary,
    "while": "while something is true",
    "else": "else something is true",
    "elif": "elif something is true",
    "print": "print something",
    "in": "in something",
}

for name, descriptsion in glossary.items():
    print(name + ": " + descriptsion)
