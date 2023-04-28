"""
Title: 
Date: 2023-04-26 11:38:34
LastEditTime: 2023-04-26 11:42:29
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


from random import choice


letters_and_numbers = (
    "a",
    "d",
    "c",
    "g",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
)
prize = ""
for i in range(4):
    prize += choice(letters_and_numbers)

print("The winning lottery number is: " + prize)

my_ticket = "0219"

times = 0
while prize != my_ticket:
    prize = ""
    for i in range(4):
        prize += choice(letters_and_numbers)
    times += 1

print(f"It took {times} times to win the lottery.")
