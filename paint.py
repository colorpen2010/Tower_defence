import pygame

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
        igrik = i['rect'].y - (model.toweronisreximus2.kartinka.get_height() - i['rect'].height)
        if i['building'] == 'tower':
            i['tower'].drawer(screen, i['rect'].x, igrik)
        if i['building']=='blue_portal':
            screen.blit(model.blue_portalius2.kartinka,[i['rect'].x,igrik])
        if i['building']=='red_portal':
            model.animated_red_portal.paint(i['rect'].x,igrik)



    # рисование башни на квадрате с мышкой
    j = model.poisk_kletki(pygame.mouse.get_pos())
    igrik = j['rect'].y - (model.toweronisreximus2.kartinka.get_height() - j['rect'].height)
    if j['type'] == 'g' and j['building']==False:
        model.apple.drawer(screen,j['rect'].x,igrik)
        # screen.blit(model.toweronisreximus2.kartinka, [j[0].x, igrik])
    else:
        screen.blit(model.toweronisreximus2.zapreshenaia_kartinka, [j['rect'].x, igrik])


if model.perecluthatel:
    for o in model.regeneration.spisoc:
        pygame.draw.rect(screen, [255, 0, 0], o[0], 3)

screen.blit(model.imaging, [100, imx])
imx += 0.5
