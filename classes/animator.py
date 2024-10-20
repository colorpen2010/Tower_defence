import pygame
from pygame.examples.vgrade import timer

import kakoito_resizer,os

class Animator:
    def __init__(self,pyt,mili_sec,map):
        spisok = []
        file_list = os.listdir(pyt)
        for p in file_list:
            spisok.append(pyt+'/' + p)
        self.map=map
        self.pictures=spisok
        self.pictures.sort(reverse=True)
        self.one=0
        self.wrema=pygame.event.custom_type()
        pygame.time.set_timer(self.wrema, mili_sec)
        self.imaging_this_beautiful_image=[]
        self.resizer()


    def control_center(self,events):
        for o in events:
            if o.type == self.wrema:
                self.smena_kartinki()
    def smena_kartinki(self):
        if len(self.pictures)-1>self.one:
                self.one+=1
        else:
            self.one=0
    def resizer(self):
        for o in self.pictures:
            self.imaging_this_beautiful_image.append(kakoito_resizer.creating_objects(o, self.map))





    def paint(self,x,bottom):
        screen=pygame.display.get_surface()
        screen.blit(self.imaging_this_beautiful_image[self.one],[x,bottom - self.imaging_this_beautiful_image[self.one].get_height()])
