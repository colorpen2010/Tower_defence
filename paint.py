import random, pygame, entity

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
    for i in model.regeneration.spisoc:
        # ровно устанавливает башню по низу клетки
        igrik = i[0].y - (model.toweronisreximus2.kartinka.get_height() - i[0].height)
        if i[0].collidepoint(pygame.mouse.get_pos()):
            if i[1] == 'g':
                screen.blit(model.toweronisreximus2.kartinka, [i[0].x, igrik])
            elif i[1] == 's':
                screen.blit(model.toweronisreximus2.zapreshenaia_kartinka, [i[0].x, igrik])
        if i[2] == True:
            print('realy')
            screen.blit(model.toweronisreximus2.kartinka, [i[0].x, igrik])
    if model.perecluthatel:
        for o in model.regeneration.spisoc:
            pygame.draw.rect(screen, [255, 0, 0], o[0], 3)

    screen.blit(model.imaging, [100, imx])
    imx += 0.5
