import pygame
from classes import messenger

class HP_system(pygame.Rect):
    def __init__(self,max_hp,tec_hp,x,y,width,height,owner=None,nohp_color=[255,0,0],hp_color=[0,255,0]):
        self.max_hp,self.tec_hp,self.width=max_hp,tec_hp,width
        self.nohp_color,self.hp_color=nohp_color,hp_color
        self.owner=owner
        self.width2=width

        self.hp_changing(0)

        pygame.Rect.__init__(self,x,y,width,height)

    def paint(self):
        screen=pygame.display.get_surface()
        pygame.draw.rect(screen,self.nohp_color,self)
        pygame.draw.rect(screen,self.hp_color,[self.x,self.y,self.width2,self.height])

    def hp_changing(self,addhp):
        self.tec_hp+=addhp
        if self.tec_hp >= self.max_hp:
                self.tec_hp=self.max_hp
        self.width2=self.width*self.tec_hp/self.max_hp
        if self.tec_hp<=0:
            messenger.messenger.otpravit('death',self,self.owner)

    def set_max_hp(self):
        self.tec_hp=self.max_hp
