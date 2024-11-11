import pygame, tower_class


class Poison_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self):
        import model
        tower_class.towernicsemus3_alhabethangerald3.__init__(self, model.map, True,
                                                              'images/Towers/PoisonIdle_cleared/00.png')
