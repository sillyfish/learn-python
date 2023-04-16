"""
Title: 
Date: 2023-04-16 12:16:09
LastEditTime: 2023-04-16 12:16:11
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""

usernames = ["admin", "jerry", "tom", "jim", "jane"]

usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

else:
    print("We need to find some users!")
