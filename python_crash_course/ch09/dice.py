"""
Title: 
Date: 2023-04-26 11:33:41
LastEditTime: 2023-04-26 11:35:03
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-26 11:33:41
LastEditTime: 2023-04-26 11:33:44
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint

        return randint(1, self.sides)


die_6 = Die()
print("Rolling a 6-sided die 10 times:")
for i in range(10):
    print(die_6.roll_die())
print()
die_20 = Die(20)
print("Rolling a 20-sided die 10 times:")
for i in range(10):
    print(die_20.roll_die())
