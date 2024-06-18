import pygame,random

class generation():
    def __init__(self):
        self.x=0
        self.y=0
    def map_generation(self,backgrounds,image: pygame.Surface):
        screen = pygame.display.get_surface()
        msize = image.get_size()
        mapsize = screen.get_size()
        # for i in model.backgrounds:
        if self.x < mapsize[0]:

            screen.blit(random.choice(backgrounds), [self.x, self.y])
            self.x += msize[0]
        elif self.y < mapsize[1]:
            self.y += msize[1]
            self.x = 0
    def restart(self):
        self.x=0
        self.y=0