"""
Title: 
Date: 2023-05-16 12:09:15
LastEditTime: 2023-05-16 12:09:17
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def test_city_country():
    from city_functions import city_country

    assert city_country("santiago", "chile") == "Santiago, Chile"


def test_city_country_population():
    from city_functions import city_country

    assert (
        city_country("santiago", "chile", 5000000)
        == "Santiago, Chile - population 5000000"
    )
