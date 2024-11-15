import math

import pygame

class Ammunition():
    def __init__(self,pyt,x,y,to_x,to_y,skorost):
        self.x,self.y,self.to_x,self.to_y=x,y,to_x,to_y
        self.skorost=skorost
        self.bullet=pygame.image.load(pyt)

    def okraska(self,):
        screen=pygame.display.get_surface()
        screen.blit(self.bullet,[self.x,self.y])


    def controler(self,events):
        for i in events:
            if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                self.traektoria()

    def traektoria(self):
        distance=math.dist([self.x,self.y],[self.to_x,self.to_y])
        if distance!=0:
            self.x+=self.skorost
            self.y+=self.skorost
