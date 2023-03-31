"""
Title: 
Date: 2023-03-27 22:23:00
LastEditTime: 2023-03-31 13:07:47
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-03-27 22:23:00
LastEditTime: 2023-03-27 22:25:28
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-03-27 22:23:00
LastEditTime: 2023-03-27 22:23:02
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
guests = ["jordan", "kobe", "james"]
print(f"Hello, {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[1].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[2].title()}, I would like to invite you to dinner.")

print(f"{guests[1].title()} can't make it to dinner.")
guests[1] = "william"
print(f"Hello, {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[1].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[2].title()}, I would like to invite you to dinner.")
print(f"I'm going to invite {len(guests)} people to dinner.")

print("I found a bigger table.")
guests.insert(0, "jim")
guests.insert(2, "jerry")
guests.append("jimmy")
print(f"Hello, {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[1].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[2].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[3].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[4].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[5].title()}, I would like to invite you to dinner.")

print("I can only invite two people to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
print(f"Hello, {guests[0].title()}, I would like to invite you to dinner.")
print(f"Hello, {guests[1].title()}, I would like to invite you to dinner.")

guests.remove("jim")
guests.remove("jordan")
print(guests)
