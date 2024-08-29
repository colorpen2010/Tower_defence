import random, pygame, entity

import animator,os

screen = pygame.display.set_mode([800, 800])
x = 0
y = 0



imx = 100
import model


def risovanie():
    global imx
    pygame.display.flip()
    model.enemy1.paint(screen)
    screen.blit(model.background, [0, 0])
    # screen.blit(model.bpbackground5,[100,50])


    #рисование поставленных башень
    for i in model.regeneration.spisoc:
        igrik = i[0].y - (model.toweronisreximus2.kartinka.get_height() - i[0].height)
        if i[2] == 'tower':
            screen.blit(model.toweronisreximus2.kartinka, [i[0].x, igrik])
            model.animation.paint(200,200)
        if i[2]=='blue_portal':
            screen.blit(model.blue_portalius2.kartinka,[i[0].x,igrik])
        if i[2]=='red_portal':
            screen.blit(model.red_portaliuinus2.kartinka,[i[0].x,igrik])



    # рисование башни на квадрате с мышкой
    j = model.poisk_kletki(pygame.mouse.get_pos())
    igrik = j[0].y - (model.toweronisreximus2.kartinka.get_height() - j[0].height)
    if j[1] == 'g' and j[2]==False:
        screen.blit(model.toweronisreximus2.kartinka, [j[0].x, igrik])
    else:
        screen.blit(model.toweronisreximus2.zapreshenaia_kartinka, [j[0].x, igrik])


if model.perecluthatel:
    for o in model.regeneration.spisoc:
        pygame.draw.rect(screen, [255, 0, 0], o[0], 3)

screen.blit(model.imaging, [100, imx])
imx += 0.5
