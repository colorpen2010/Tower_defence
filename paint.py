import random,pygame, model

screen = pygame.display.set_mode([800, 800])
x = 0
y = 0


def risovanie():
    pygame.display.flip()
    map_generation(model.backgrounds[0], screen)


def map_generation(image: pygame.Surface, map_size: pygame.Surface):
    global x, y
    msize = image.get_size()
    mapsize = map_size.get_size()
    # for i in model.backgrounds:
    if x < mapsize[0]:

        screen.blit(random.choice(model.backgrounds), [x, y])
        x += msize[0]
    elif y < mapsize[1]:
        y += msize[1]
        x = 0
    # if y!=mapsize:
    #     screen.blit(model.background1,[x,y])
