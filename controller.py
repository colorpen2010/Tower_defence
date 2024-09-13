import time

import pygame, entity, model



def control():
    # time.sleep(0.01)
    events = pygame.event.get()

    model.animated_red_portal.control_center(events)
    model.animated_tower.control_center(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)

