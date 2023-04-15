"""
Title: 
Date: 2023-03-31 19:52:26
LastEditTime: 2023-03-31 19:52:26
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
sum = 0
for number in numbers:
    sum += number

print(sum)
