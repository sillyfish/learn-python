"""
Title: 
Date: 2023-04-16 16:29:23
LastEditTime: 2023-04-20 16:44:18
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-16 16:29:23
LastEditTime: 2023-04-16 16:32:20
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-16 16:29:23
LastEditTime: 2023-04-16 16:29:26
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
qichen = {"first_name": "qichen", "last_name": "deng", "age": 6, "city": "guangzhou"}
print(qichen)

yifeng = {"first_name": "yifeng", "last_name": "li", "age": 38, "city": "guangzhou"}
yiming = {"first_name": "yiming", "last_name": "deng", "age": 36, "city": "guangzhou"}

people = [qichen, yifeng, yiming]

for person in people:
    print()
    for key, value in person.items():
        print(key + ": " + str(value))
