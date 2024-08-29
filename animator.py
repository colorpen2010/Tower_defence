import pygame
from pygame.examples.vgrade import timer


class Animator:
    def __init__(self,pictures:list):
        self.pictures=pictures
        self.one=0

    def control_center(self,events):
        pass


    def paint(self,x,y):
        screen=pygame.display.get_surface()
        print(self.pictures)
        self.imaging_this_beautiful_image=pygame.image.load(self.pictures[self.one])

        screen.blit(self.imaging_this_beautiful_image,[x,y])
        if len(self.pictures)-1>self.one:
            self.one+=1
        else:
            self.one=0