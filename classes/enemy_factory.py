import pygame,os

from classes.animator import Animator


class enem_factory():
    def __init__(self,pyt,map,flipped=False,procent=1,mili_sec=100,scorost=5,spisok_tochek=None,x=100,bottom=175):
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
        self.center[0]=int(self.center[0])
        self.center[1]=int(self.center[1])
        self.enemy.control_center(events)
        if self.spisok_tochek!=[]:
            print(self.center)
            if self.center[0]<self.spisok_tochek[0][0]:
                if self.center[0]<=self.spisok_tochek[0][0]-self.scorost:
                    self.x+=self.scorost
                else:
                    self.x+=1
            elif self.center[1]>self.spisok_tochek[0][1]:
                if self.center[1]>=self.spisok_tochek[0][1]+self.scorost:
                    self.bottom-=self.scorost
                else:
                    self.bottom-=1
            elif self.center[0]>self.spisok_tochek[0][0]:
                if self.center[0] >= self.spisok_tochek[0][0] + self.scorost:
                    self.x-=self.scorost
                else:
                    self.x-=1
            elif self.center[1]<self.spisok_tochek[0][1]:
                if self.center[1]<=self.spisok_tochek[0][1]-self.scorost:
                    self.bottom+=self.scorost
                else:
                    self.bottom+=1
            else:
                del self.spisok_tochek[0]
            # self.center[0]=self.x
            # self.center[1]=self.bottom

    def paint(self):
        screen=pygame.display.get_surface()
        self.enemy.paint(self.x,self.bottom)