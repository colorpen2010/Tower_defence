import pygame
from classes import animator
class towernicsemus3_alhabethangerald3():
    def __init__(self,map):
        self.animated_tower= animator.Animator('images/Towers/PoisonIdle', 40, map)


    def drawer(self,screen,x,y):
        self.animated_tower.paint(x, y)

    def control_point(self,events):
        self.animated_tower.control_center(events)


