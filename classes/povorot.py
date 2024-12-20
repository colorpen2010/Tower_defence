import pygame.transform

from classes import animator


class Rotating(animator.Animator):
    def __init__(self,mili_sec,map,procent,left_pack=None,right_pack=None,up_pack=None,down_pack=None):
        assert left_pack is not None or right_pack is not None, "cocacola ili babaji"
        assert up_pack is not None or down_pack is not None, "babaji ili fortinaiti"
        animator.Animator.__init__(self,left_pack,mili_sec,map,procent=procent)
        self.way=0
        self.down_pack=[down_pack,False]
        self.up_pack=[up_pack,False]
        self.left_pack=[left_pack,False]
        self.right_pack=[right_pack,False]
        if self.right_pack[0] is None:
            self.right_pack[0]=self.left_pack[0]
            self.right_pack[1]=True
        if self.left_pack[0] is None:
            self.left_pack[0]=self.right_pack[0]
            self.left_pack[1]=True
        if self.up_pack[0] is None:
            self.up_pack[0]=self.down_pack[0]
            self.up_pack[1]=True
        if self.down_pack[0] is None:
            self.down_pack[0] =self.up_pack[0]
            self.down_pack[1]=True

    def move_down(self):
        if self.way!=0:
            self.imaging_this_beautiful_image=self.downloader(self.down_pack[0],self.map,self.procent,False,False,'y',self.down_pack[1])
            self.one=0
            self.way=0
    def move_up(self):
        if self.way!=2:
            self.imaging_this_beautiful_image=self.downloader(self.up_pack[0],self.map,self.procent,False,False,'y',self.up_pack[1])
            self.one = 0
            self.way =2
    def move_left(self):
        if self.way!=1:
            self.imaging_this_beautiful_image=self.downloader(self.left_pack[0],self.map,self.procent,False,self.left_pack[1])
            self.one = 0
            self.way =1
    def move_right(self):
        if self.way!=3:
            self.imaging_this_beautiful_image=self.downloader(self.right_pack[0],self.map,self.procent,False,self.right_pack[1])
            self.one = 0
            self.way =3