import pygame

class HP_system():
    def __init__(self,max_hp,tec_hp,x,y,width,height,nohp_color=[255,0,0],hp_color=[0,255,0]):
        self.max_hp,self.tec_hp,self.width=max_hp,tec_hp,width
        self.nohp_color,self.hp_color=nohp_color,hp_color

        self.nohp_bar=pygame.Rect(x,y,width,height)
        self.hp_bar=pygame.Rect(x,y,width*tec_hp/max_hp,height)



    def paint(self):
        screen=pygame.display.get_surface()
        pygame.draw.rect(screen,self.nohp_color,self.nohp_bar)
        pygame.draw.rect(screen,self.hp_color,self.hp_bar)

    def hp_changing(self,addhp):
        self.tec_hp+=addhp
        if self.tec_hp >= self.max_hp:
                self.tec_hp=self.max_hp
        self.hp_bar.width=self.width*self.tec_hp/self.max_hp