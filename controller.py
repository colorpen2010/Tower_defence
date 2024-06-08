import pygame.display
events=pygame.event.get()
def control():
    for o in events:
        if o.type == pygame.QUIT:
            exit()