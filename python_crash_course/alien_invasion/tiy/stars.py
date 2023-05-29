from random import randint
from typing import Any

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.size = 50
        self.image = pygame.transform.scale(
            pygame.image.load("../images/star.jpeg"), (self.size, self.size)
        )
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.tick = 0

    def random(self):
        self.rect.x = self.x + randint(0 - self.size, self.size)
        self.rect.y = self.y + randint(0 - self.size, self.size)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.random()


pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

stars = pygame.sprite.Group()
star_height, stars_width = 50, 50
current_x, current_y = 0, 0

while current_y < (screen.get_rect().height - star_height):
    while current_x < (screen.get_rect().width - stars_width):
        star = Star(current_x, current_y)
        stars.add(star)
        current_x += 2 * stars_width
    current_x = 0
    current_y += 2 * star_height


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((246, 246, 246))

    stars.draw(screen)
    pygame.display.flip()
    clock.tick(0.5)
    stars.update()
