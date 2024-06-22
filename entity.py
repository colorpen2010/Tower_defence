import pygame,random

class generation():
    def __init__(self):
        self.x=0
        self.y=0
        self.cordinatssave=[]
    def map_generation(self,backgrounds,screen,image: pygame.Surface):
        # screen = pygame.display.get_surface()
        msize = image.get_size()
        mapsize = screen.get_size()
        # for i in model.backgrounds:
        if self.cordinatssave!=None:
            if self.x < mapsize[0]:

                screen.blit(random.choice(backgrounds), [self.x, self.y])
                self.x += msize[0]
                self.cordinatssave.append([self.x,self.y])
                print('eve')
            elif self.y < mapsize[1]:
                self.y += msize[1]
                self.x = 0
                self.cordinatssave.append([self.x,self.y])
                print('yiy')
        else:
            for o in self.cordinatssave:

                pass
    def restart(self):
        self.x=0
        self.y=0