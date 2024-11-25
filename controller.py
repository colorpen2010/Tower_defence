import pygame, model
from classes import warehouse

def control():
    events = pygame.event.get()

    if model.apple!=None:
        model.apple.control_point(events)
    for r in model.spisoc:
        if r.tower!= None:
            r.tower.control_point(events)

    model.animated_blue_portal.control_center(events)
    model.animated_red_portal.control_center(events)
    if model.bullet!=None:
        model.bullet.controler(events)

    for q in model.bazar:
        q.controller(events)


    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_SPACE:
            for i in model.spisoc:
                if i.tower!=None:
                    model.bullet = warehouse.Ammunition('images/ammo/PoisonTower.png', i.x, i.y, 500, 500, 1)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.KEYDOWN and o.key == pygame.K_r:
            model.wallet.otnimanie(-1000)
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_ESCAPE:
            model.apple=None
