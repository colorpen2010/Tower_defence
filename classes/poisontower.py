import model
from classes import tower_class,warehouse


class Poison_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self,x,bottom,dont_shoot=False):
        tower_class.towernicsemus3_alhabethangerald3.__init__(self,model.enemys,200, len(model.house), True,x,bottom,
                                                              'images/Towers/PoisonIdle_cleared/00.png',dont_shoot=dont_shoot,)
    def vistrel(self,enemy_coordinations=[500,500]):
        model.bullets.append(warehouse.Ammunition(0.4,'images/ammo/PoisonTower.png',len(model.house), self.get_center()[0], self.get_center()[1] ,enemy_coordinations[0], enemy_coordinations[1], 2.55))

