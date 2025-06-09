import pygame
from classes import enemy_factory, messenger,hp_System,timer_launcher


class Wave():
    def __init__(self, tec_level, types):
        self.tec_level = tec_level
        self.enemys = []
        self.types = types
        self.ev = pygame.event.custom_type()
        self.enemy_changing()
        self.bullets = []

        # timer_launcher.timer_worker.create_timer(self.ev, 3000,self.smena_i_spawn)
        if 'spawn_speed' in self.enemy_settings:
            timer_launcher.timer_worker.delete_timer(self.ev)
            timer_launcher.timer_worker.create_timer(self.ev, self.enemy_settings['spawn_speed'], self.smena_i_spawn)
        else:
            timer_launcher.timer_worker.delete_timer(self.ev)
            timer_launcher.timer_worker.create_timer(self.ev, 3000, self.smena_i_spawn)
        messenger.messenger.podpisatsa(self.messages)

    def enemy_creating(self, type, hp, damage,speed=None, ret=False):
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
        def_sps={'blue':2.45,'green':1.50,'purple':0.50,'red':0.80}
        if speed is None:
            speed=def_sps[type]
        if type == 'blue':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True,
                                               [0.5, 0.5, 0.5, 0.5], scorost=speed,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-damage, hp=hp)
        elif type == 'purple':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True, [1, 1, 1, 1],
                                               scorost=speed,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-damage, hp=hp)
        elif type == 'green':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True,
                                               [0.9, 0.9, 0.4, 0.4],
                                               scorost=speed,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-damage, hp=hp)
        elif type == 'red':
            enemy = enemy_factory.enem_factory(type, self.tec_level.give_your_number_of_etashey(), True,
                                               [0.8, 0.8, 0.8, 0.8], scorost=speed,
                                               spisok_tochek=self.tec_level.route.copy(), damage=-damage, hp=hp)
        if enemy != None and ret is False:
            self.enemys.append(enemy)
        else:
            return enemy

    def paint(self):
        for m in self.bullets:
            m.okraska()

    def controller(self, events):
        for m in self.bullets:
            m.controler(events)
        for p in self.enemys:
            p.control(events)

        # for o in events:
            #таймер

    def smena_i_spawn(self):
        if self.count <= 0 and self.types != []:
            # print(self.count, self.types)
            del self.types[0]
            self.enemy_changing()
        else:
            self.enemy_spawning()

    def enemy_spawning(self):
        if len(self.types)!=0:
            if self.count > 0:
                speed=self.enemy_settings['speed'] if 'speed' in self.enemy_settings else None
                self.enemy_creating(self.enemy_type, self.enemy_settings['hp'],self.enemy_settings['damage'],speed)
                self.count -= 1
                print('spawned enemy ' + self.enemy_type)




    def enemy_changing(self):
        if len(self.types) !=0:
            self.first_enemy = self.types[0]
            # self.next_enemy = self.types[1]
            self.enemy_type = list(self.first_enemy.keys())[0]
            self.enemy_settings = self.first_enemy[self.enemy_type]
            # self.next_enemy_type = list(self.next_enemy.keys())[0]
            # self.next_enemy_settings = self.types[1][self.next_enemy_type]
            self.count = self.enemy_settings['count']
            print(self.first_enemy, self.enemy_type, self.enemy_settings)
            if 'spawn_speed' in self.enemy_settings:
                timer_launcher.timer_worker.delete_timer(self.ev)
                timer_launcher.timer_worker.create_timer(self.ev, self.enemy_settings['spawn_speed'],
                                                         self.smena_i_spawn)
                print('spawn speed: ' + str(self.enemy_settings['spawn_speed']))

            else:
                timer_launcher.timer_worker.delete_timer(self.ev)
                timer_launcher.timer_worker.create_timer(self.ev, 3000, self.smena_i_spawn)
                print('spawn speed: 3000')
    def messages(self, pismo, otpravitel, dop_info):
        if pismo == 'bullet_at_pos' and otpravitel in self.bullets:
            # print('B.A.P')
            otpravitel.kill_me()
            self.bullets.remove(otpravitel)
        if pismo == 'bullet_letit' and otpravitel in self.bullets:
            for i in self.enemys:
                if i.get_rect().collidepoint(otpravitel.x, otpravitel.y):
                    hp_System.HP_system.hp_changing(i.hp, -  otpravitel.damage)
                    otpravitel.kill_me()
                    self.bullets.remove(otpravitel)
                    break
        if pismo == 'enemy_at_end' and otpravitel in self.enemys:
            # print('E.A.E')
            otpravitel.kill_me()
            self.enemys.remove(otpravitel)
            self.tec_level.mainhp.hp_changing(dop_info)
            self.level_switch()
        if pismo == 'death' and dop_info in self.enemys:
            dop_info.kill_me()
            self.enemys.remove(dop_info)
            self.tec_level.wallet.otnimanie(-15)
            self.level_switch()


    def level_switch(self):
        if self.count == 0 and len(self.enemys) == 0 and len(self.types) == 0:
            messenger.messenger.otpravit('wave_no_enemys', self)