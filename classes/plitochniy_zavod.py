import time

import pygame,random,os

import kakoito_resizer


class Tsekh:
    def __init__(self,type,x,y,map):
        self.type=type
        self.nothing=pygame.Surface([100,100])
        rect=pygame.Rect(0,0,100,100)
        pygame.draw.rect(self.nothing,[255,255,255],rect,50)
        pygame.draw.rect(self.nothing,[255,0,0],rect,10)
        pygame.image.save(self.nothing,'no_image.png')
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
            self.plitka=kakoito_resizer.creating_objects(path,map)
        else:
            self.nothing=kakoito_resizer.creating_objects('no_image.png',map)

        pass

    def get_product_size(self):
        if self.no_image==False:
            return self.plitka.get_size()
        else:
            return self.nothing.get_size()

    def okraska(self,screen):
        # screen=pygame.display.get_surface()
        if self.no_image==False:
            screen.blit(self.plitka,[self.x,self.y])
        else:
            screen.blit(self.nothing,[self.x,self.y])