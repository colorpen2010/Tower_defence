import image_worker, pygame, os, kakoito_resizer
from classes import animator

class towernicsemus3_alhabethangerald3():
    def __init__(self, map,reversed,x,bottom,pyt='images/Images_for_tests/tower/Tower_Entity.png'):
        self.shop=None
        self.pyt=pyt
        self.x=x
        self.bottom=bottom
        self.reversed=reversed
        self.screen = pygame.display.get_surface()
        self.image=kakoito_resizer.creating_objects_x(pyt, map)
        self.animated_tower = animator.Animator(os.path.dirname(pyt), 40, map,self.reversed,x=x,bottom=bottom)
        self.zapreshenaia_kartinka = image_worker.to_grayscale_with_color(self.image,[255,0,0])
        pygame.image.save(self.zapreshenaia_kartinka, 'test1.png')

    def paint(self):
        self.animated_tower.paint()
    def colored_drawer(self, colored=False, prozrathnost=150):
        if not colored:
            image = image_worker.poly_prosrathnost(self.image, prozrathnost)
            self.screen.blit(image, [self.x, self.bottom - image.get_height()])
        else:
            zapreshenaia_kartinka = image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, prozrathnost)
            self.screen.blit(zapreshenaia_kartinka, [self.x, self.bottom-zapreshenaia_kartinka.get_height()])

    def control_point(self, events):
        self.animated_tower.control_center(events)

