"""
Title: 
Date: 2023-04-16 16:02:40
LastEditTime: 2023-04-16 16:06:43
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
current_users = ["admin", "joe", "jane", "jim", "jill"]
new_users = ["joe", "Jane", "Jim", "jill", "jack"]

for user in new_users:
    if user in current_users:
        print(f"{user} is already taken.")
    else:
        print(f"{user} is available.")

# case insensitive
print("\ncase insensitive")
for user in new_users:
    if user.lower() in [current.lower() for current in current_users]:
        print(f"{user} is already taken.")
    else:
        print(f"{user} is available.")
