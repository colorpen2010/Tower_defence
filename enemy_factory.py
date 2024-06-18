import pygame
class enem_factory():
    def __init__(self,enemy_image):
        self.enemy=enemy_image
    def enemy(self):
        return
    def control(self):
        return
    def paint(self):
        screen=pygame.display.get_surface()
        screen.blit(self.enemy, [50,400],[0,0,100,100])