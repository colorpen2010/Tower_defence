import pygame
fontik=pygame.font.SysFont('Arial',120,True)

class Magazin():
    def __init__(self,x,y,pyt,price,towar,click_def):

        self.x,self.y=x,y
        if price>999 and price< 1000000:
            price=str(round(price/1000,1))+'K'
        elif price>999999:
            price=str(round(price/1000000,1))+'M'
        self.selected=False
        self.price=fontik.render('$'+str(price),True,[0,0,0])
        self.image=pygame.image.load(pyt)
        self.image.blit(self.price,[self.image.get_width()/2-self.price.get_width()/2,590])
        self.image=pygame.transform.scale(self.image,[self.image.get_width()/7,self.image.get_height()/7])
        self.image_rect=pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())

    def controller(self,events):
        event=events
        for o in event:
            if o.type == pygame.MOUSEBUTTONDOWN and self.image_rect.collidepoint(o.pos):
                self.selected= not self.selected


    def paint(self):
        screen=pygame.display.get_surface()
        screen.blit(self.image,[self.x,self.y])