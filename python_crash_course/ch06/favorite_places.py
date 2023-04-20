"""
Title: 
Date: 2023-04-20 16:46:16
LastEditTime: 2023-04-20 16:50:25
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-20 16:46:16
LastEditTime: 2023-04-20 16:46:19
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
favorite_places = {
    "qichen": ["guangzhou", "shenzhen", "beijing"],
    "deng": ["beijing"],
    "dengqichen": ["guangzhou", "shenzhen"],
}

for name, places in favorite_places.items():
    print(name + ":")
    for place in places:
        print("\t" + place)
