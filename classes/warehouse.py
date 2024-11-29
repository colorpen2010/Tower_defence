import math,math_utils

import pygame,time
from numpy.ma.core import angle


class Ammunition():
    def __init__(self,pyt,x,y,to_x,to_y,skorost):
        self.x,self.y,self.to_x,self.to_y=x,y,to_x,to_y
        self.fly=True
        self.mouse_mode = False
        self.skorost=skorost
        self.bullet=pygame.image.load(pyt)
        self.bullet2=pygame.image.load(pyt)
        self.wrema=pygame.event.custom_type()
        pygame.time.set_timer(self.wrema, 10)
    def okraska(self,):
        screen=pygame.display.get_surface()
        screen.blit(self.bullet2,[self.x,self.y])


    def controler(self,events):
        for i in events:
            if i.type == pygame.KEYDOWN and i.key == pygame.K_e:
                self.mouse_mode= not self.mouse_mode
            if self.fly and i.type == self.wrema:
                self.traektoria()
        if self.mouse_mode:
            self.to_x=pygame.mouse.get_pos()[0]
            self.to_y=pygame.mouse.get_pos()[1]


    def traektoria(self):
        distance=math.dist([self.x,self.y],[self.to_x,self.to_y])
        angle=math_utils.get_angle_by_point([self.x, self.y], [self.to_x, self.to_y])
        if distance>0:
            self.x,self.y=math_utils.get_point_by_angle([self.x,self.y],angle,self.skorost)
            self.bullet2=pygame.transform.rotate(self.bullet,angle+90)