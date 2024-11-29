import pygame

import kakoito_resizer

pygame.init()
screen = pygame.display.set_mode([900, 800])
font = pygame.font.SysFont('arial', 50)
x = 0
y = 0



imx = 100
import model


def risovanie():
    global imx
    model.clock.tick()
    fps=model.clock.get_fps()
    pygame.display.flip()
    model.enemy1.paint(screen)
    for p in model.spisoc:
        p.okraska(screen)

    #снаряды


    #надписи
    for g in model.bazar:
        g.paint(model.wallet.money>=g.numprice)
    model.wallet.grafiti(800,0)


    #рисование поставленных башень

    for i in model.spisoc:
        if i.building == 'tower':
            i.tower.drawer()
        if i.building== 'red_portal':
            model.animated_red_portal.paint(i.x,i.get_rect().bottom)
        if i.building== 'blue_portal':
            model.animated_blue_portal.paint(i.x,i.get_rect().bottom)

    # рисование башни на квадрате с мышкой
    j = model.poisk_kletki(pygame.mouse.get_pos())
    if j!=None and model.apple!=None:
        rect=j.get_rect()
        if j.type == 'grass' and j.building==None:
            model.apple.colored_drawer(prozrathnost=200)
        else:
            model.apple.colored_drawer(True)

        if model.perecluthatel:
            show_fps=font.render(str(int(fps)),True,[255,0,0])
            screen.blit(show_fps,[10,20])

    for m in model.bullets:
        m.okraska()


screen.blit(model.imaging, [100, imx])
imx += 0.5
