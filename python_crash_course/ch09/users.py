"""
Title: 
Date: 2023-04-26 10:55:36
LastEditTime: 2023-04-26 10:58:23
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""
"""
Title: 
Date: 2023-04-26 10:55:36
LastEditTime: 2023-04-26 10:55:38
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Login attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User("John", "Doe")
u1.describe_user()
u1.greet_user()
u2 = User("Jane", "Doe")
u2.describe_user()
u2.greet_user()

print(f"u1's login attempts: {u1.login_attempts}")
print("Incrementing login attempts...3 times")
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(f"now, u1's login attempts: {u1.login_attempts}")
print("Resetting login attempts...")
u1.reset_login_attempts()
print(f"now, u1's login attempts: {u1.login_attempts}")
