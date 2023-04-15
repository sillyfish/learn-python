"""
Title: 
Date: 2023-03-31 19:28:12
LastEditTime: 2023-04-01 13:42:06
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-03-31 19:28:12
LastEditTime: 2023-03-31 19:28:13
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
pizzas = ["pepperoni", "cheese", "mushroom"]
for pizza in pizzas:
    print(f"i like {pizza} pizza.")

print("i really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append("sausage")
friend_pizzas.append("pineapple")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
