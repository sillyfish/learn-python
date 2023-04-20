"""
Title: 
Date: 2023-04-20 16:53:24
LastEditTime: 2023-04-20 16:53:26
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
cities = {
    "guangzhou": {
        "country": "china",
        "population": 10000000,
        "fact": "a beautiful city",
    },
    "beijing": {
        "country": "china",
        "population": 20000000,
        "fact": "a historical city",
    },
    "new york": {"country": "america", "population": 30000000, "fact": "a big city"},
}

for city, info in cities.items():
    print(city.title() + ":")
    for key, value in info.items():
        print("\t" + key + ": " + str(value))
