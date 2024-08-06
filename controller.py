import time

import pygame,entity,model
def control():
    # time.sleep(0.01)
    events = pygame.event.get()
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type==pygame.KEYDOWN and o.key==pygame.K_SPACE:
            model.regeneration.restart()
            model.regeneration.map_generation()
        if o.type==pygame.KEYDOWN and o.key==pygame.K_TAB:
            model.perecluthatel= not model.perecluthatel
        if o.type==pygame.MOUSEBUTTONDOWN and o.button==pygame.BUTTON_LEFT:
            model.change=True
