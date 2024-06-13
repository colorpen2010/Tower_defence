import pygame
def control():
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()