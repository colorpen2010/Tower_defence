import pygame,os

from classes import animator,povorot,messenger,hp_System,timer_launcher

class enem_factory():
    def __init__(self,type,map,flipped=False,procents=[1,1,1,1],mili_sec=100,scorost=5,spisok_tochek=None,damage=50,hp=50):
        self.damage=damage
        self.walking=pygame.event.custom_type()
        timer_launcher.timer_worker.create_timer(self.walking,30)
        self.x=spisok_tochek[0][0]
        self.bottom=spisok_tochek[0][1]
        self.enemy=povorot.Rotating(mili_sec,map,procents,'images/Monsters/move/'+type+'_left',up_pack='images/Monsters/move/'+type+'_up',down_pack='images/Monsters/move/'+type+'_down',x=self.x,bottom=self.bottom+(800/map/2))
        self.spisok_tochek=spisok_tochek
        self.scorost=scorost
        self.enemy.set_center(spisok_tochek[0][0],spisok_tochek[0][1])
        self.hp=hp_System.HP_system(hp,hp,self.x,self.enemy.get_rect().y,self.get_rect().width,5,self)
        # self.povort=povorot.Rotating()\

        # self.enemy=pygame.transform.flip(flipped,False)
    # def enemy(self):z
    #     return
    def control(self,events):
        self.center=self.enemy.get_center()
        self.center[0]=int(self.center[0])
        self.center[1]=int(self.center[1])
        self.enemy.control_center(events)
        for o in events:
            if self.spisok_tochek!=[] and o.type == self.walking:
                if self.center[0]<self.spisok_tochek[0][0]:
                    self.enemy.move_right()
                    if self.center[0]<=self.spisok_tochek[0][0]-self.scorost:
                        self.enemy.x+=self.scorost
                    else:
                        self.enemy.set_center(self.spisok_tochek[0][0])
                elif self.center[1]>self.spisok_tochek[0][1]:
                    self.enemy.move_up()
                    if self.center[1]>=self.spisok_tochek[0][1]+self.scorost:
                        self.enemy.bottom-=self.scorost
                    else:
                        self.enemy.set_center(center_y=self.spisok_tochek[0][1])
                elif self.center[0]>self.spisok_tochek[0][0]:
                    self.enemy.move_left()
                    if self.center[0] >= self.spisok_tochek[0][0] + self.scorost:
                        self.enemy.x-=self.scorost
                    else:
                        self.enemy.set_center(self.spisok_tochek[0][0])
                elif self.center[1]<self.spisok_tochek[0][1]:
                    self.enemy.move_down()
                    if self.center[1]<=self.spisok_tochek[0][1]-self.scorost:
                        self.enemy.bottom+=self.scorost
                    else:
                        self.enemy.set_center(center_y=self.spisok_tochek[0][1])
                else:
                    del self.spisok_tochek[0]
                if len(self.spisok_tochek)==0:
                    messenger.messenger.otpravit('enemy_at_end',self,self.damage)

            # self.center[0]=self.x
            # self.center[1]=self.bottom

# label = text()
    def paint(self,debug=False):
        self.hp.centerx,self.hp.y=self.enemy.get_center()[0],self.get_rect().y-5
        if debug:
            pass
        self.hp.paint()
        self.enemy.paint(debug)

    def get_center(self):
        return self.enemy.get_center()

    def get_rect(self):
        return  self.enemy.get_rect()