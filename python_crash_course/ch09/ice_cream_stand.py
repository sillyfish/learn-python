"""
Title: 
Date: 2023-04-26 11:09:36
LastEditTime: 2023-04-26 11:09:39
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def show_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ics = IceCreamStand("The Old Mill", "American")
ics.show_flavors()
