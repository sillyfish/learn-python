"""
Title: 
Date: 2023-04-21 21:28:59
LastEditTime: 2023-04-21 21:29:01
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
sandwich_orders = [
    "sandwich1",
    "pastrami",
    "sandwich2",
    "sandwich3",
    "pastrami",
    "pastrami",
]

print("the deli has run out of pastrami.")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == "pastrami":
        continue
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}.")
