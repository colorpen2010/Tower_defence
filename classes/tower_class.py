import image_worker, pygame, os, kakoito_resizer
from classes import animator
# print(os.path.dirname('images/Images_for_tests/tower/Tower_Entity.png'))
# print(os.path.basename('images/Images_for_tests/tower/Tower_Entity.png'))


class towernicsemus3_alhabethangerald3():
    def __init__(self, map,pyt='images/Images_for_tests/tower/Tower_Entity.png'):
        self.screen = pygame.display.get_surface()
        self.image=kakoito_resizer.creating_objects(pyt,map)
        self.animated_tower = animator.Animator(os.path.dirname(pyt), 40, map)
        self.zapreshenaia_kartinka = image_worker.to_grayscale(self.image)
        pygame.image.save(self.zapreshenaia_kartinka, 'test1.png')

    def drawer(self, x, y):
        self.animated_tower.paint(x, y)

    def colored_drawer(self, x, y, colored=False, prozrathnost=150):
        if not colored:
            image = image_worker.poly_prosrathnost(self.image, prozrathnost)
            self.screen.blit(image,[x,y])
        else:
            zapreshenaia_kartinka = image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, prozrathnost)
            self.screen.blit(zapreshenaia_kartinka, [x, y])

    def control_point(self, events):
        self.animated_tower.control_center(events)
