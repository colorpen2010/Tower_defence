import model
from classes import tower_class,warehouse


class Poison_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self,x,bottom):
        import model
        tower_class.towernicsemus3_alhabethangerald3.__init__(self, len(model.house), True,x,bottom,
                                                              'images/Towers/PoisonIdle_cleared/00.png')
    def vistrel(self,enemy_coordinations=[500,500]):
        return (warehouse.Ammunition(0.4,'images/ammo/PoisonTower.png',len(model.house), self.x, self.bottom-50, enemy_coordinations[0], enemy_coordinations[1], 1))

