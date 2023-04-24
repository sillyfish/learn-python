"""
Title: 
Date: 2023-04-21 20:45:50
LastEditTime: 2023-04-21 20:45:52
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
