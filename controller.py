import pygame.display
events=pygame.event
def control():
    for o in events:
        if o.type == pygame.QUIT:
            exit()