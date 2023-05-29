import sys
import pygame


from python_crash_course.alien_invasion.image import Image


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


rokect = Image("../images/rocket.png", (116, 300))
rokect.place_center(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill("grey")

    keys = pygame.key.get_pressed()
    screen_rect = screen.get_rect()
    if keys[pygame.K_RIGHT] and rokect.rect.right < screen_rect.right:
        rokect.rect.x += 5
    if keys[pygame.K_LEFT] and rokect.rect.left > 0:
        rokect.rect.x -= 5
    if keys[pygame.K_UP] and rokect.rect.top > 0:
        rokect.rect.y -= 5
    if keys[pygame.K_DOWN] and rokect.rect.bottom < screen_rect.bottom:
        rokect.rect.y += 5

    screen.blit(rokect.image, rokect.rect)

    pygame.display.flip()
    clock.tick(60)
