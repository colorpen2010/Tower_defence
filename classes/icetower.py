from classes import tower_class


class Ice_tower(tower_class.towernicsemus3_alhabethangerald3):
    def __init__(self):
        import model
        tower_class.towernicsemus3_alhabethangerald3.__init__(self, len(model.house), False,
                                                              'images/Towers/IceIdle_cleared/00.png')
