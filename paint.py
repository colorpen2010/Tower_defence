import random,pygame, model,entity

screen = pygame.display.set_mode([800, 800])
x = 0
y = 0


def risovanie():
    pygame.display.flip()
    model.regeneration.map_generation(model.backgrounds,model.backgrounds[0])
    model.enemy1.paint()



    # if y!=mapsize:
    #     screen.blit(model.background1,[x,y])
