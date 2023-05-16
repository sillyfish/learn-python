"""
Title: 
Date: 2023-05-16 12:03:00
LastEditTime: 2023-05-16 12:03:02
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def city_country(city, country, population=0):
    if population > 0:
        return f"{city.title()}, {country.title()} - population {str(population)}"
    else:
        return f"{city.title()}, {country.title()}"
