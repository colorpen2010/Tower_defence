import pygame, model
from classes import warehouse
from classes.firetower import Fire_tower
from classes.poisontower import Poison_tower


def control():
    events = pygame.event.get()

    if model.apple!=None:
        model.apple.control_point(events)
    for r in model.plitki:
        if r.tower!= None:
            r.tower.control_point(events)

    for p in model.enemys:
        p.control(events)

    if model.animated_blue_portal!=None:
        model.animated_blue_portal.control_center(events)
    if model.animated_red_portal!=None:
        model.animated_red_portal.control_center(events)
    for m in model.bullets:
        m.controler(events)

    for q in model.bazar:
        q.controller(events)


    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_SPACE:
            for i in model.plitki:
                if i.tower!=None:
                    model.bullets.append(i.tower.vistrel())
        if o.type==pygame.MOUSEMOTION and model.apple!=None:
            i = model.poisk_kletki(pygame.mouse.get_pos())
            model.apple.x=i.x
            model.apple.bottom=i.get_rect().bottom
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.KEYDOWN and o.key == pygame.K_r:
            model.wallet.otnimanie(-1000)
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_ESCAPE:
            model.apple=None
