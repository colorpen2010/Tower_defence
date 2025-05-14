import pygame

pygame.init()


class Knopka():
    def __init__(self, x, y, pyt,daystvie, size=(50, 50)):
        self.deystvitel=daystvie
        self.size = size
        self.kartinka = pygame.image.load(pyt)
        self.rect=pygame.rect.Rect(x,y,size[0],size[1])
        self.remake = pygame.transform.scale(self.kartinka, size)
        self.y = y
        self.x = x

    def risyem(self, screen):
        screen.blit(self.remake, [self.x, self.y])
    def event(self,events:list):
        for o in events:
            if o.type==pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(o.pos):
                self.deystvitel()
                events.remove(o)
