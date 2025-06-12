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
    images += model.tec_wave.enemys
    model.tec_level.paint(model.perecluthatel, images)
    model.tec_wave.paint(model.perecluthatel)
    # model.normal.risyem(screen)
    # model.speed.risyem(screen)
    # model.super_speed.risyem(screen)
    model.time_button.risovanie()

    for g in model.bazar:
        g.paint(model.tec_level.wallet.money >= g.numprice)
    model.tec_level.wallet.grafiti(800, 0)



    # рисование башни на квадрате с мышкой
    j = model.tec_level.poisk_kletki(pygame.mouse.get_pos())
    if j != None and model.apple != None:
        rect = j.get_rect()
        if j.type == 'grass' and j.building == None:
            model.apple.colored_drawer(prozrathnost=200)
        else:
            model.apple.colored_drawer(True)



        show_fps = font.render(str(int(fps)), True, [255, 0, 0])
        screen.blit(show_fps, [10, 20])


