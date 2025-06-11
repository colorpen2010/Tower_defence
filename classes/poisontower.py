import model
from classes import tower_class,warehouse
import model


class Poison_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self,x,bottom,visota,dont_shoot=False):
        self.visota = visota
        tower_class.towernicsemus3_alhabethangerald3.__init__(self,model.tec_wave.enemys,visota, True,x,bottom,
                                                              'images/Towers/PoisonIdle_cleared/00.png',dont_shoot=dont_shoot,)
    def vistrel(self,enemy_coordinations=[500,500]):
        model.tec_wave.bullets.append(warehouse.Ammunition(0.4,'images/ammo/PoisonTower.png',self.visota, self.get_center()[0], self.get_center()[1] ,enemy_coordinations[0], enemy_coordinations[1], 0.02,2))

