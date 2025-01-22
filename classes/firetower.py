from classes import tower_class,warehouse
import model


class Fire_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self,x,bottom):
        import model
        tower_class.towernicsemus3_alhabethangerald3.__init__(self,len(model.house),False,x,bottom,'images/Towers/FireIdle_cleared/00.png')
    def vistrel(self):
        return (warehouse.Ammunition(0.2,'images/ammo/FireTower.png',len(model.house), self.x, self.bottom-50, 500, 500, 2))
