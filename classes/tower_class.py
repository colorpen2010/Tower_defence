import image_worker, pygame
from classes import animator


class towernicsemus3_alhabethangerald3():
    def __init__(self, map):
        self.animated_tower = animator.Animator('images/Towers/PoisonIdle', 40, map)

    def drawer(self, x, y):
        self.animated_tower.paint(x, y)

    def colored_drawer(self,pyt, x, y, colored=False, prozrathnost=150):
        image=pygame.image.load(pyt)
        screen = pygame.display.get_surface()
        if colored:
            self.zapreshenaia_kartinka = image_worker.to_grayscale(image)
        else:
            self.zapreshenaia_kartinka = image
        self.zapreshenaia_kartinka = image_worker.poly_prosrathnost(self.zapreshenaia_kartinka, prozrathnost)
        screen.blit(self.zapreshenaia_kartinka, [x, y])

    def control_point(self, events):
        self.animated_tower.control_center(events)
