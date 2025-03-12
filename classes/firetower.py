from classes import tower_class,warehouse
import model


class Fire_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self,x,bottom,dont_shoot=False):
        import model
        tower_class.towernicsemus3_alhabethangerald3.__init__(self,len(model.house),False,x,bottom,
                                                              'images/Towers/FireIdle_cleared/00.png',dont_shoot=dont_shoot)
    def vistrel(self):
        model.bullets.append(warehouse.Ammunition(0.2,'images/ammo/FireTower.png',len(model.house), self.get_center()[0], self.get_center()[1], 500, 500, 2))
