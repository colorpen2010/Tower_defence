import pygame

import kakoito_resizer
import math_utils

pygame.init()
screen = pygame.display.set_mode([900, 800])
font = pygame.font.SysFont('arial', 50)

import model


def risovanie():
    model.clock.tick()
    fps = model.clock.get_fps()
    pygame.display.flip()


    # надписи

    images = []
    images += model.enemys
    model.tec_level.paint(model.perecluthatel, images)

    for g in model.bazar:
        g.paint(model.wallet.money >= g.numprice)
    model.wallet.grafiti(800, 0)



    # рисование башни на квадрате с мышкой
    j = model.tec_level.poisk_kletki(pygame.mouse.get_pos())
    if j != None and model.apple != None:
        rect = j.get_rect()
        if j.type == 'grass' and j.building == None:
            model.apple.colored_drawer(prozrathnost=200)
        else:
            model.apple.colored_drawer(True)

    if model.perecluthatel:
        shoti = 0
        for u in model.route:
            pygame.draw.circle(screen, [0, 0, 0], u, 10)
            pos = font.render(str(shoti), True, [255, 0, 0])
            screen.blit(pos, u)
            shoti += 1

        show_fps = font.render(str(int(fps)), True, [255, 0, 0])
        screen.blit(show_fps, [10, 20])

    for m in model.bullets:
        m.okraska()
