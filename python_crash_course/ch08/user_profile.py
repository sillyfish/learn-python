"""
Title: 
Date: 2023-04-24 12:14:51
LastEditTime: 2023-04-24 12:14:53
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


print(build_profile("albert", "einstein", location="princeton", field="physics"))
print(build_profile("Yiming", "Deng", Age="37", City="Guangzhou", Country="China"))
