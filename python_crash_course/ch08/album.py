"""
Title: 
Date: 2023-04-24 11:46:25
LastEditTime: 2023-04-24 11:46:27
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""


def make_album(singer, album, number=""):
    album_dict = {"singer": singer, "album": album}
    if number:
        album_dict["number"] = number
    return album_dict


while True:
    print("Please enter the album info:")
    print("(enter 'q' at any time to quit)")
    singer = input("singer: ")
    if singer == "q":
        break
    album = input("album: ")
    if album == "q":
        break
    print(make_album(singer, album))
