import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
surfrect = surface.get_rect()
rect = pygame.Rect((0, 0), (128, 128))
rect.center = (surfrect.w / 2, surfrect.h / 2)
touched = False
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(ev.pos):
                touched = True
                # This is the starting point
                pygame.mouse.get_rel()
        elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False
    clock.tick(60)
    surface.fill((0, 0, 0))
    if touched:
        rect.move_ip(pygame.mouse.get_rel())
        rect.clamp_ip(surfrect)
    surface.fill((255, 255, 255), rect)
    pygame.display.flip()
import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))

ball = pygame.image.load("pydroball.png")
ballrect = ball.get_rect()
clock = pygame.time.Clock()

width = surface.get_width()
height = surface.get_height()

speed = [4, 4]
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    clock.tick(60)
    surface.fill((0, 0, 0))
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    surface.blit(ball, ballrect)
    pygame.display.flip()

