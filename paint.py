import random,pygame, model,entity

screen = pygame.display.set_mode([800, 800])
x = 0
y = 0

imx=100

def risovanie():
    global imx
    pygame.display.flip()
    model.regeneration.map_generation(model.backgrounds,model.backgrounds[0])
    model.enemy1.paint()
    screen.blit(model.imaging,[100,imx])
    imx+=0.5



    # if y!=mapsize:
    #     screen.blit(model.background1,[x,y])
