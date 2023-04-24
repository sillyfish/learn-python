"""
Title: 
Date: 2023-04-21 21:17:20
LastEditTime: 2023-04-21 21:19:50
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-21 21:17:20
LastEditTime: 2023-04-21 21:17:22
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
while True:
    toppings = input("Enter a pizza toppings: ")
    if toppings == "quit":
        break
    print("We'll add " + toppings + " to your pizza.")

toppings = ""
while toppings != "quit":
    toppings = input("Enter a pizza toppings again: ")
    print("We'll add " + toppings + " to your pizza.")
