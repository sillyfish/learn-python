"""
Title: 
Date: 2023-04-26 10:50:40
LastEditTime: 2023-04-26 10:52:05
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


restaurant = Restaurant("The Old Mill", "American")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

r1 = Restaurant("Big House", "Chinese")
r1.describe_restaurant()
r2 = Restaurant("Little House", "Japanese")
r2.describe_restaurant()
r3 = Restaurant("Middle House", "Korean")
r3.describe_restaurant()

restaurant = Restaurant("The Old Mill", "American")
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)
