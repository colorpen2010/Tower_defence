import pygame,os

from classes.animator import Animator


class enem_factory():
    def __init__(self,pyt,map,flipped=False,procent=0.5,mili_sec=100):
        self.enemy=Animator(os.path.dirname(pyt),mili_sec,map,procent)
        # self.enemy=pygame.transform.flip(flipped,False)
    # def enemy(self):
    #     return
    def control(self,events):
        self.enemy.control_center(events)
    def paint(self):
        screen=pygame.display.get_surface()
        self.enemy.paint(100,400)