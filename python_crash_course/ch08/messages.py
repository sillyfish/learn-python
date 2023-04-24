"""
Title: 
Date: 2023-04-24 12:00:11
LastEditTime: 2023-04-24 12:01:08
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def show_messages(messages):
    for message in messages:
        print(message)


messages = ["Hello", "How are you?", "Goodbye"]
show_messages(messages)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


sent_messages = []
send_messages(messages, sent_messages)
print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")

new_messages = ["Hello", "How are you?", "Goodbye"]
send_messages(new_messages[:], sent_messages)
print(f"new_messages: {new_messages}")
print(f"sent_messages: {sent_messages}")
