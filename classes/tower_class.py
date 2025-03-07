import image_worker, pygame, os, kakoito_resizer
from classes import animator,warehouse

class towernicsemus3_alhabethangerald3():
    def __init__(self, map,reversed,x,bottom,pyt='images/Images_for_tests/tower/Tower_Entity.png',milisec=3000,dont_shoot=False):
        self.shop=None
        self.pyt=pyt
        self.x=x

        self.dont_shoot=dont_shoot
        self.event=pygame.event.custom_type()
        self.milisec=milisec
        pygame.time.set_timer(self.event,self.milisec)

        self.bottom=bottom
        self.reversed=reversed
        self.screen = pygame.display.get_surface()
        self.image=kakoito_resizer.creating_objects_x(pyt, map)
        self.animated_tower = animator.Animator(os.path.dirname(pyt), 40, map,self.reversed,x=x,bottom=bottom)
        self.zapreshenaia_kartinka = image_worker.to_grayscale_with_color(self.image,[255,0,0])
        pygame.image.save(self.zapreshenaia_kartinka, 'test1.png')

    def get_center(self):
        return self.animated_tower.get_center()
    def paint(self):
        self.animated_tower.paint()
    def colored_drawer(self, colored=False, prozrathnost=150):
        if not colored:
            image = image_worker.poly_prosrathnost(self.image, prozrathnost)
            self.screen.blit(image, [self.x, self.bottom - image.get_height()])
        else:
            zapreshenaia_kartinka = image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, prozrathnost)
            self.screen.blit(zapreshenaia_kartinka, [self.x, self.bottom-zapreshenaia_kartinka.get_height()])

    def control_point(self, events,):

        for o in events:
            if o.type==self.event and self.dont_shoot==False:
                self.vistrel()
                print('working')
        self.animated_tower.control_center(events)
    def vistrel(self,enemy_coordinations=[500,500]):
        print('this is not good')
        pass

