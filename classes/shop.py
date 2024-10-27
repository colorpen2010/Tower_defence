import pygame
fontik=pygame.font.SysFont('Arial',10)

class Magazin():
    def __init__(self,x,y,pyt,price):
        self.x,self.y=x,y
        self.price=fontik.render(str(price),True,[0,0,0])
        self.image=pygame.image.load(pyt)
        self.image=pygame.transform.scale(self.image,[self.image.get_width()/7,self.image.get_height()/7])
        self.image.blit(self.price,[10,20])

    def paint(self):
        screen=pygame.display.get_surface()
        screen.blit(self.image,[self.x,self.y])