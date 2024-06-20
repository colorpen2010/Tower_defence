import time

import pygame,entity,model
def control():
    time.sleep(0.01)
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type==pygame.KEYDOWN and o.key==pygame.K_SPACE:
            model.regeneration.restart()
            model.regeneration.map_generation(model.backgrounds, model.backgrounds[0])
