"""
Title: 
Date: 2023-05-16 15:17:59
LastEditTime: 2023-05-16 15:18:01
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


import pytest


@pytest.fixture
def employee():
    from employee import Employee

    employee = Employee("joe", "smith", 10000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 15000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 20000
