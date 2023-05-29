from typing import Any

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("../images/rain.jpg"), (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += 3


pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

raindrops = pygame.sprite.Group()
raindrop_height, raindrop_width = 50, 50
current_x, current_y = 0, 0

while current_y < (screen.get_rect().height - raindrop_height):
    while current_x < (screen.get_rect().width - raindrop_width):
        raindrop = Raindrop(current_x, current_y)
        raindrops.add(raindrop)
        current_x += 2 * raindrop_width
    current_x = 0
    current_y += 2 * raindrop_height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((246, 246, 246))

    raindrops.update()
    raindrops.draw(screen)
    for raindrop in raindrops.sprites():
        if raindrop.rect.y >= screen.get_rect().height:
            # raindrops.remove(raindrop)
            raindrop.rect.y = 0
    pygame.display.flip()
    clock.tick(60)
