"""
Title: 
Date: 2023-04-24 11:40:33
LastEditTime: 2023-04-24 11:40:35
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def make_shirt(size: str, text: str = "I love Python."):
    print(f"the size of the shirt is {size}, and the text is {text}.")


make_shirt("L", "I love Python.")
make_shirt(text="I love Python.", size="L")

make_shirt("L")
make_shirt("M")
make_shirt("S", "I love C++.")
