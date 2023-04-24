"""
Title: 
Date: 2023-04-24 12:17:22
LastEditTime: 2023-04-24 12:18:50
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-24 12:17:22
LastEditTime: 2023-04-24 12:17:25
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
