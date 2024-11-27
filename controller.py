import pygame, model
from classes import warehouse
from classes.firetower import Fire_tower
from classes.poisontower import Poison_tower


def control():
    events = pygame.event.get()

    if model.apple!=None:
        model.apple.control_point(events)
    for r in model.spisoc:
        if r.tower!= None:
            r.tower.control_point(events)

    model.animated_blue_portal.control_center(events)
    model.animated_red_portal.control_center(events)
    for m in model.bullets:
        m.controler(events)

    for q in model.bazar:
        q.controller(events)


    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_SPACE:
            for i in model.spisoc:
                print(i.tower)
                if type(i.tower) is Poison_tower:
                    model.bullets.append(warehouse.Ammunition('images/ammo/PoisonTower.png', i.x, i.y, 500, 500, 1))
                elif type(i.tower) is Fire_tower:
                    model.bullets.append(warehouse.Ammunition('images/ammo/FireTower.png', i.x, i.y, 500, 500, 2))
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.KEYDOWN and o.key == pygame.K_r:
            model.wallet.otnimanie(-1000)
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_ESCAPE:
            model.apple=None
