import pygame
from classes import enemy_factory, messenger


class Wave():
    def __init__(self, tec_level, types):
        self.tec_level = tec_level
        self.enemys = []
        self.types = types
        self.ev = pygame.event.custom_type()
        self.enemy_changing()

        pygame.time.set_timer(self.ev, 3000)
        messenger.messenger.podpisatsa(self.messages)

    def enemy_creating(self, type, hp, ret=False):
        """
        есть 4 вида противника:
        blue,
        purple,
        green,
        red.

        there are 4 types of enemy:
        blue,
        green,
        purple,
        red.
        :param type:
        :return:
        """
        enemy = None
        if type == 'blue':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True,
                                               [0.5, 0.5, 0.5, 0.5], scorost=2.45,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-5, hp=hp)
        elif type == 'purple':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True, [1, 1, 1, 1],
                                               scorost=0.50,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-20, hp=hp)
        elif type == 'green':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True,
                                               [1, 1, 0.5, 0.5],
                                               scorost=1.50,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-10, hp=hp)
        elif type == 'red':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True,
                                               [0.8, 0.8, 0.8, 0.8], scorost=0.8,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-15, hp=hp)
        if enemy != None and ret is False:
            self.enemys.append(enemy)
        else:
            return enemy

    def controller(self, events):
        for p in self.enemys:
            p.control(events)
        for o in events:
            #таймер
            if o.type == self.ev:
                if self.count <= 0 and self.types != []:
                    # print(self.count, self.types)
                    del self.types[0]
                    self.enemy_changing()

                self.enemy_spawning()

    def enemy_spawning(self):
        if self.types != {}:
            if self.count > 0:
                self.enemy_creating(self.enemy_type, self.enemy_settings['hp'])
                self.count -= 1

    def enemy_changing(self):
        if self.types != []:
            self.first_enemy = self.types[0]
            self.enemy_type = list(self.first_enemy.keys())[0]
            self.enemy_settings = self.first_enemy[self.enemy_type]
            self.count = self.enemy_settings['count']
            print(self.first_enemy, self.enemy_type, self.enemy_settings)
    def messages(self, pismo, otpravitel, dop_info):
        global map_number, config, tec_level
        if pismo == 'enemy_at_end':
            # print('E.A.E')
            self.enemys.remove(otpravitel)
            tec_level.mainhp.hp_changing(dop_info)
        if pismo == 'death':
            self.enemys.remove(dop_info)
            tec_level.wallet.otnimanie(-15)
