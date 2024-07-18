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
        if i.collidepoint(pygame.mouse.get_pos()):
            igrik =i.y-(model.toweronisreximus2.backgrounds.get_height()-i.height)
            screen.blit(model.toweronisreximus2.backgrounds,[i.x,igrik])
            print(i)
    if model.perecluthatel:
        for o in model.regeneration.spisoc:
            pygame.draw.rect(screen, [255, 0, 0], o, 3)
    screen.blit(model.imaging, [100, imx])
    imx += 0.5

    # if y!=mapsize:
    #     screen.blit(model.background1,[x,y])
