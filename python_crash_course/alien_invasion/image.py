"""
Title: 
Date: 2023-05-19 10:36:18
LastEditTime: 2023-05-19 10:36:20
Category: 
Tags: 
Slug: 
Authors: 惊人不易
Summary: 
"""

import pygame


class Image:
    def __init__(self, path, size) -> None:
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def placeCenter(self, screen):
        self.rect.center = screen.get_rect().center
        screen.blit(self.image, self.rect)
