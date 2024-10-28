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


    #надписи
    model.magaz.paint()
    model.magaz2.paint()
    model.magaz3.paint()
    model.magaz4.paint()


    #рисование поставленных башень

    for i in model.spisoc:
        if i.building == 'tower':
            i.tower.drawer( i.x,i.get_rect().bottom)
        if i.building== 'red_portal':
            model.animated_red_portal.paint(i.x,i.get_rect().bottom)
        if i.building== 'blue_portal':
            model.animated_blue_portal.paint(i.x,i.get_rect().bottom)

    # рисование башни на квадрате с мышкой
    j = model.poisk_kletki(pygame.mouse.get_pos())
    if j!=None:
        rect=j.get_rect()
        if j.type == 'grass' and j.building==False:
            model.apple.colored_drawer(j.x,rect.bottom ,prozrathnost=200)
        else:
            model.apple.colored_drawer(j.x, rect.bottom,True)

        if model.perecluthatel:
            show_fps=font.render(str(int(fps)),True,[255,0,0])
            screen.blit(show_fps,[10,20])

screen.blit(model.imaging, [100, imx])
imx += 0.5
