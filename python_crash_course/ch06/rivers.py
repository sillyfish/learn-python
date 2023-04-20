"""
Title: 
Date: 2023-04-20 16:24:29
LastEditTime: 2023-04-20 16:24:31
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
rivers = {"nile": "egypt", "changjiang": "china", "huanghe": "china"}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for river in rivers.values():
    print(river.title())
