import image_worker, pygame, os, kakoito_resizer
from classes import animator

class towernicsemus3_alhabethangerald3():
    def __init__(self, map,pyt='images/Images_for_tests/tower/Tower_Entity.png'):
        self.screen = pygame.display.get_surface()
        self.image=kakoito_resizer.creating_objects(pyt,map)
        self.animated_tower = animator.Animator(os.path.dirname(pyt), 40, map,False)
        self.zapreshenaia_kartinka = image_worker.to_grayscale(self.image)
        pygame.image.save(self.zapreshenaia_kartinka, 'test1.png')

    def drawer(self, x, bottom):
        self.animated_tower.paint(x, bottom)

    def colored_drawer(self, x, bottom, colored=False, prozrathnost=150):
        if not colored:
            image = image_worker.poly_prosrathnost(self.image, prozrathnost)
            self.screen.blit(image, [x, bottom - image.get_height()])
        else:
            zapreshenaia_kartinka = image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, prozrathnost)
            self.screen.blit(zapreshenaia_kartinka, [x, bottom-zapreshenaia_kartinka.get_height()])

    def control_point(self, events):
        self.animated_tower.control_center(events)
