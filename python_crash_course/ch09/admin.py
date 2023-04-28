"""
Title: 
Date: 2023-04-26 11:18:04
LastEditTime: 2023-04-26 11:18:06
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


from users import User


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.p = Privileges()

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

    def show_p(self):
        print("Admin privileges with Privaileges attribute:")
        for privilege in self.p.privileges:
            print(f"- {privilege}")


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


a1 = Admin("John", "Doe")
a1.show_privileges()
a1.show_p()
