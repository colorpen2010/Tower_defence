import pygame,os

from classes.animator import Animator


class enem_factory():
    def __init__(self,pyt,map,flipped=False,procent=0.5,mili_sec=100,scorost=5,spisok_tochek=None,x=100,bottom=175):
        self.enemy=Animator(os.path.dirname(pyt),mili_sec,map,procent=procent)
        self.spisok_tochek=spisok_tochek
        self.x=x
        self.scorost=scorost
        self.bottom=bottom

        # self.enemy=pygame.transform.flip(flipped,False)
    # def enemy(self):z
    #     return
    def control(self,events):
        self.center=self.enemy.get_center(self.x,self.bottom)
        self.enemy.control_center(events)
        if self.spisok_tochek!=[]:
            print(self.center)
            if self.center[0]<=self.spisok_tochek[0][0]:
                self.x+=self.scorost
            elif self.center[1]>=self.spisok_tochek[0][1]:
                self.bottom-=self.scorost
            elif self.center[0]>=self.spisok_tochek[0][0]:
                self.x-=self.scorost
            elif self.center[1]<=self.spisok_tochek[0][1]:
                self.bottom+=self.scorost
            else:
                del self.spisok_tochek[0]
            # self.center[0]=self.x
            # self.center[1]=self.bottom

    def paint(self):
        screen=pygame.display.get_surface()
        self.enemy.paint(self.x,self.bottom)