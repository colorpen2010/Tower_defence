import pygame
from pygame.examples.vgrade import timer


class Animator:
    def __init__(self,pictures:list,mili_sec):
        self.pictures=pictures
        self.pictures.sort(reverse=True)
        self.one=0
        self.wrema=pygame.event.custom_type()
        pygame.time.set_timer(self.wrema, mili_sec)

    def control_center(self,events):
        for o in events:
            if o.type == self.wrema:
                self.smena_kartinki()
    def smena_kartinki(self):
        if len(self.pictures)-1>self.one:
                self.one+=1
        else:
            self.one=0



    def paint(self,x,y):
        screen=pygame.display.get_surface()
        self.imaging_this_beautiful_image=pygame.image.load(self.pictures[self.one])

        screen.blit(self.imaging_this_beautiful_image,[x,y])
