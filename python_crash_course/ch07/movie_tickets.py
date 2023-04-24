"""
Title: 
Date: 2023-04-21 21:20:13
LastEditTime: 2023-04-21 21:20:15
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
age = 0
while age >= 0:
    age = input("Enter your age: ")
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
