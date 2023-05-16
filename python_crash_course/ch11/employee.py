"""
Title: 
Date: 2023-05-16 15:14:12
LastEditTime: 2023-05-16 15:14:14
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        self.annual_salary += raise_amount
