import math,math_utils
from classes import messenger

import pygame,time
from numpy.ma.core import angle

import kakoito_resizer


class Ammunition():
    def __init__(self,size,pyt,map,x,y,to_x,to_y,skorost):
        self.x,self.y=x,y
        self.start_pos=[x,y]
        self.end_pos=[to_x,to_y]
        self.fly=True
        self.mouse_mode = False
        self.skorost=skorost
        self.bullet=kakoito_resizer.creating_objects_x(pyt, map, size)
        self.bullet2=self.bullet
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
            self.end_pos[0]=pygame.mouse.get_pos()[0]
            self.end_pos[1]=pygame.mouse.get_pos()[1]


    def traektoria(self):
        distance=math.dist([self.x,self.y],self.end_pos)
        start_distance=math.dist(self.start_pos,self.end_pos)
        angle=math_utils.get_angle_by_point([self.x, self.y], self.end_pos)
        if distance<start_distance:
            self.x,self.y=math_utils.get_point_by_angle([self.x,self.y],angle,self.skorost)
            self.bullet2=pygame.transform.rotate(self.bullet,angle+90)
        else:
            messenger.messenger.otpravit('bullet_at_target',self)
