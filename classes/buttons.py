import pygame

pygame.init()


class Knopka():
    def __init__(self, x, y, pyt,deystvie, size=(50, 50),dop_info={}):
        self.deystvitel=deystvie
        self.dop_info=dop_info
        self.size = size
        self.kartinka = pygame.image.load(pyt)
        self.rect=pygame.rect.Rect(x,y,size[0],size[1])
        self.remake = pygame.transform.scale(self.kartinka, size)
        self.y = y
        self.x = x

    def risyem(self, screen):
        screen.blit(self.remake, [self.x, self.y])
    def controller(self,events:list):
        for o in events:
            if o.type==pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(o.pos):
                self.deystvitel(**self.dop_info)
                events.remove(o)
