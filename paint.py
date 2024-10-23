import pygame

import kakoito_resizer

pygame.init()
screen = pygame.display.set_mode([800, 800])
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



    #рисование поставленных башень
    # for i in model.regeneration.spisoc:
    #     igrik = i['rect'].y - (model.toweronisreximus2.kartinka.get_height() - i['rect'].height)
    #     if i['building'] == 'tower':
    #         i['tower'].drawer( i['rect'].x, igrik)
    #     if i['building']=='blue_portal':
    #         screen.blit(model.blue_portalius2.kartinka,[i['rect'].x,igrik])
    #     if i['building']=='red_portal':
    #         model.animated_red_portal.paint(i['rect'].x,igrik)

    for i in model.spisoc:
        if i.building == 'tower':
            i.tower.drawer( i.x,i.get_rect().bottom)
        if i.building== 'red_portal':
            model.animated_red_portal.paint(i.x,i.get_rect().bottom)
        if i.building== 'blue_portal':
            model.animated_blue_portal.paint(i.x,i.get_rect().bottom)
        # if i['building']=='blue_portal':
            # screen.blit(model.blue_portalius2.kartinka,[i['rect'].x,igrik])
    #     if i['building']=='red_portal':
    #         model.animated_red_portal.paint(i['rect'].x,igrik)

    # рисование башни на квадрате с мышкой
    j = model.poisk_kletki(pygame.mouse.get_pos())
    if j!=None:
        rect=j.get_rect()
        if j.type == 'grass' and j.building==False:
            # print(j.x)
            model.apple.colored_drawer(j.x,rect.bottom ,prozrathnost=200)
        else:
            model.apple.colored_drawer(j.x, rect.bottom,True)

        if model.perecluthatel:
            show_fps=font.render(str(int(fps)),True,[255,0,0])
            screen.blit(show_fps,[10,20])

screen.blit(model.imaging, [100, imx])
imx += 0.5
