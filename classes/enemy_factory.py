import pygame,os

from classes import animator,povorot

class enem_factory():
    def __init__(self,type,map,flipped=False,procent=1,mili_sec=100,scorost=5,spisok_tochek=None,x=100,bottom=175):
        self.enemy=povorot.Rotating(mili_sec,map,procent,'images/Monsters/move/'+type+'_left',up_pack='images/Monsters/move/'+type+'_up',down_pack='images/Monsters/move/'+type+'_down')

        self.spisok_tochek=spisok_tochek
        self.x=x
        self.scorost=scorost
        self.bottom=bottom
        # self.povort=povorot.Rotating()

        # self.enemy=pygame.transform.flip(flipped,False)
    # def enemy(self):z
    #     return
    def control(self,events):
        self.center=self.enemy.get_center()
        self.center[0]=int(self.center[0])
        self.center[1]=int(self.center[1])
        self.enemy.control_center(events)
        if self.spisok_tochek!=[]:
            if self.center[0]<self.spisok_tochek[0][0]:
                self.enemy.move_right()
                if self.center[0]<=self.spisok_tochek[0][0]-self.scorost:
                    self.enemy.x+=self.scorost
                else:
                    self.enemy.x+=1
            elif self.center[1]>self.spisok_tochek[0][1]:
                self.enemy.move_up()
                if self.center[1]>=self.spisok_tochek[0][1]+self.scorost:
                    self.enemy.bottom-=self.scorost
                else:
                    self.enemy.bottom-=1
            elif self.center[0]>self.spisok_tochek[0][0]:
                self.enemy.move_left()
                if self.center[0] >= self.spisok_tochek[0][0] + self.scorost:
                    self.x-=self.scorost
                else:
                    self.x-=1
            elif self.center[1]<self.spisok_tochek[0][1]:
                self.enemy.move_down()
                if self.center[1]<=self.spisok_tochek[0][1]-self.scorost:
                    self.enemy.bottom+=self.scorost
                else:
                    self.enemy.bottom+=1
            else:
                del self.spisok_tochek[0]
            # self.center[0]=self.x
            # self.center[1]=self.bottom

# label = text()
    def paint(self):
        screen=pygame.display.get_surface()
        self.enemy.paint()