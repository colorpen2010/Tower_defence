import pygame
from pygame.examples.vgrade import timer

import kakoito_resizer,os

class Animator:
    def __init__(self,pyt,mili_sec,map,reverse=False,procent=1,x=700,bottom=775):
        self.procent=procent
        self.map=map
        self.x,self.bottom=x,bottom
        self.one=0
        self.wrema=pygame.event.custom_type()
        pygame.time.set_timer(self.wrema, mili_sec)
        self.imaging_this_beautiful_image=self.downloader(pyt,map,procent,reverse,True)

    @staticmethod
    def downloader(pyt,map,procent,reverse,flip,flip_y=False):
        spisok=[]
        imaging_this_beautiful_image=[]
        file_list = os.listdir(pyt)
        for p in file_list:
            spisok.append(pyt+'/' + p)
        spisok.sort(reverse=reverse)
        for o in spisok:
            imaging_this_beautiful_image.append(pygame.transform.flip(kakoito_resizer.creating_objects_x(o, map, procent), flip, flip_y))
        return imaging_this_beautiful_image



    def control_center(self,events):
        for o in events:
            if o.type == self.wrema:
                self.smena_kartinki()
    def smena_kartinki(self):
        if len(self.imaging_this_beautiful_image)-1>self.one:
                self.one+=1
        else:
            self.one=0
    def get_center(self):
        center=[]
        center.append(self.x+self.imaging_this_beautiful_image[self.one].get_size()[0] / 2)
        center.append(self.bottom-self.imaging_this_beautiful_image[self.one].get_size()[1] / 2)
        return center

    def set_center(self,center_x,center_y=None):
        self.x=center_x-self.imaging_this_beautiful_image[self.one].get_size()[0] / 2
        if center_y!=None:
            self.bottom=center_y+(self.imaging_this_beautiful_image[self.one].get_size()[1] / 2)





    def paint(self):
        screen=pygame.display.get_surface()
        screen.blit(self.imaging_this_beautiful_image[self.one],[self.x,self.bottom - self.imaging_this_beautiful_image[self.one].get_height()])
        # pygame.draw.circle(screen,[255,0,0],self.get_center(),10)
