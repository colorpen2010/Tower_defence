import pygame,random,os

import kakoito_resizer


class Tsekh:
    def __init__(self,type,x,y,map):
        # self.plitka=pygame.Surface([50,50])
        self.x,self.y=x,y
        path = 'images/Tiles/' + type + '_0' + str(random.randint(1, 4)) + '.png'
        print(path)

        while os.path.exists(path)==False:
            path='images/Tiles/'+type+'_0'+str(random.randint(1,4))+'.png'
            print(path)

        self.plitka=kakoito_resizer.creating_objects(path,map)

        pass

    def okraska(self):
        screen=pygame.display.get_surface()
        screen.blit(self.plitka,[self.x,self.y])