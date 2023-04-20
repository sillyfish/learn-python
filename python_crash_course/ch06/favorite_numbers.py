"""
Title: 
Date: 2023-04-20 15:16:03
LastEditTime: 2023-04-20 15:17:30
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-20 15:16:03
LastEditTime: 2023-04-20 15:16:05
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
favorite_numbers = {
    "qichen": [6, 10],
    "deng": [5],
    "dengqichen": [4, 17],
    "dengqichendeng": [3],
    "dengqichendengqichen": [2, 4, 6, 8],
}
print(favorite_numbers)
for name, numbers in favorite_numbers.items():
    print(name + ":")
    for number in numbers:
        print("\t" + str(number))
