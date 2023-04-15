"""
Title: 
Date: 2023-03-31 19:58:30
LastEditTime: 2023-03-31 19:58:30
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

print(f"the first three items in the list are: {cubes[:3]}")
print(f"Three items from the middle of the list are: {cube[4:7]}")
print(f"The last three items in the list are: {cubes[-3:]}")
