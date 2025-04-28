import pygame, model, math_utils
from classes import warehouse
from classes.firetower import Fire_tower
from classes.poisontower import Poison_tower

ev = pygame.event.custom_type()



def control():
    global count, enemy_type, first_enemy, enemy_settings
    events = pygame.event.get()
    if model.apple != None:
        model.apple.control_point(events)
    for r in model.tec_level.plitki:
        if r.tower != None:
            r.tower.control_point(events)

        # print(count)
    model.tutorial_wave.controller(events)
    # print(b)
    # count= types['green'][0]

    # count-=1

    for p in model.enemys:
        p.control(events)

    model.tec_level.controller(events)
    for m in model.bullets:
        m.controler(events)

    for q in model.bazar:
        q.controller(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_SPACE:
            for i in model.plitki:
                if i.tower != None:
                    i.tower.vistrel()



        if o.type == pygame.KEYDOWN and o.key == pygame.K_UP:
            model.mainhp.hp_changing(15)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_DOWN:
            model.mainhp.hp_changing(-15)

        if o.type == pygame.KEYDOWN and o.key == pygame.K_1:
            print('spawned monster_blue')
            pygame.display.set_mode([2000, 2000])
            # model.enemy_creating('blue')
        if o.type == pygame.KEYDOWN and o.key == pygame.K_2:
            print('spawned monster_purple')
            model.enemy_creating('purple',2)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_3:
            print('spawned monster_green')
            model.enemy_creating('green',2)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_4:
            print('spawned monster_red')
            model.enemy_creating('red',2)

        if o.type == pygame.MOUSEMOTION and model.apple != None:
            i = model.tec_level.poisk_kletki(pygame.mouse.get_pos())
            if i != None:
                model.apple.x = i.x
                model.apple.bottom = i.get_rect().bottom
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.KEYDOWN and o.key == pygame.K_r:
            model.wallet.otnimanie(-1000)
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)
        if o.type == pygame.KEYDOWN and o.key == pygame.K_ESCAPE:
            model.apple = None
