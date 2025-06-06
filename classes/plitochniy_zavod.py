import time

import pygame,random,os

import kakoito_resizer

nothing = pygame.Surface([100, 100])

rect = pygame.Rect(0, 0, 100, 100)
pygame.draw.rect(nothing, [255, 255, 255], rect, 50)
pygame.draw.rect(nothing, [255, 0, 0], rect, 10)
pygame.image.save(nothing, 'no_image.png')

class Tsekh:
    def __init__(self,type,x,y,colithestvo_etashey):
        self.building=None
        self.type=type
        self.tower=None
        attempt=0
        self.no_image=False
        # self.plitka=pygame.Surface([50,50])
        self.x,self.y=x,y
        path = 'images/Tiles/' + type + '_0' + str(random.randint(1, 4)) + '.png'

        while os.path.exists(path)==False and self.no_image==False:
            path='images/Tiles/'+type+'_0'+str(random.randint(1,4))+'.png'
            attempt+=1
            if attempt==50:
                self.no_image=True
            if attempt==100:
                raise Exception('Ошибка 404 Объект не найден "'+path+'"')

        if self.no_image==False:
            self.plitka=kakoito_resizer.creating_objects_x(path, colithestvo_etashey)
        else:
            self.nothing=kakoito_resizer.creating_objects_x('no_image.png', colithestvo_etashey)

        pass

    def get_product_size(self):
        if self.no_image==False:
            return self.plitka.get_size()
        else:
            return self.nothing.get_size()
    def get_rect(self):
        return pygame.Rect([self.x,self.y],self.get_product_size())

    def paint_tower(self,debug):
        if self.tower!=None:
            self.tower.paint(debug)



    def okraska(self,screen):
        # screen=pygame.display.get_surface()
        if self.no_image==False:
            screen.blit(self.plitka,[self.x,self.y])
        else:
            screen.blit(self.nothing,[self.x,self.y])