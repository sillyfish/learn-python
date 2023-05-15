"""
Title: 
Date: 2023-05-15 12:05:17
LastEditTime: 2023-05-15 12:05:17
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def check_num(num):
    try:
        num = int(num)
    except ValueError:
        print("Please input a number!")
        return False
    else:
        return True


nums = []
while True:
    if len(nums) == 0:
        num = input("Please input a number: ")
    elif len(nums) == 1:
        num = input("Please input another number: ")
    else:
        print(int(nums[0]) + int(nums[1]))
        break
    if not check_num(num):
        continue
    nums.append(num)
