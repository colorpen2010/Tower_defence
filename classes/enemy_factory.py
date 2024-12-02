import pygame,os

from classes.animator import Animator


class enem_factory():
    def __init__(self,pyt,map,flipped=False):
        self.enemy=Animator(os.path.dirname(pyt),10,map)
        # self.enemy=pygame.transform.flip(flipped,False)
    def enemy(self):
        return
    def control(self):
        return
    def paint(self):
        screen=pygame.display.get_surface()
        self.enemy.paint(100,400)