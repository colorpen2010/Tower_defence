import pygame, math_utils, yaml, os

from classes import hp_System, enemy_factory, shop, wallet, firetower, poisontower, \
    stormtower, icetower, messenger, level


def vibor_bashni(bashnia, shop):
    global apple
    i = tec_level.poisk_kletki(pygame.mouse.get_pos())
    if shop.numprice <= wallet.money:
        apple = bashnia(i.x, i.get_rect().bottom, tec_level.give_your_number_of_etashey(), True)
        apple.shop = shop


def ystanowka_bashni(pos):
    global apple
    i = tec_level.poisk_kletki(pos)
    if i.type == 'grass' and apple != None and wallet.money >= apple.shop.numprice and i.building == None:
        wallet.otnimanie(apple.shop.numprice)
        i.building = 'tower'
        tyipiok = type(apple)
        i.tower = tyipiok(i.x, i.get_rect().bottom, tec_level.give_your_number_of_etashey())
        if wallet.money < apple.shop.numprice:
            apple = None


def enemy_creating(type, hp):
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
        enemy = enemy_factory.enem_factory(type, tec_level.give_your_number_of_etashey(), True,
                                           [0.5, 0.5, 0.5, 0.5], scorost=2.45,
                                           spisok_tochek=tec_level.route.copy(), damage=-5, hp=hp)
    elif type == 'purple':
        enemy = enemy_factory.enem_factory(type, tec_level.give_your_number_of_etashey(), True, [1, 1, 1, 1],
                                           scorost=0.50,
                                           spisok_tochek=tec_level.route.copy(), damage=-20, hp=hp)
    elif type == 'green':
        enemy = enemy_factory.enem_factory(type, tec_level.give_your_number_of_etashey(), True, [1, 1, 0.5, 0.5],
                                           scorost=1.50,
                                           spisok_tochek=tec_level.route.copy(), damage=-10, hp=hp)
    elif type == 'red':
        enemy = enemy_factory.enem_factory(type, tec_level.give_your_number_of_etashey(), True,
                                           [0.8, 0.8, 0.8, 0.8], scorost=0.8,
                                           spisok_tochek=tec_level.route.copy(), damage=-15, hp=hp)
    if enemy != None:
        enemys.append(enemy)

def try_to_load_config(number):
    if os.path.exists("levels/map_" + str(number) + ".yaml"):
        f = open("levels/map_" + str(map_number) + ".yaml", 'r', encoding="utf-8")
        config = yaml.safe_load(f)
        print(config)
        wallet.set_money(100)
        mainhp.set_max_hp()
        return level.Level(config['map'])
    else:
        return None

def messages(pismo, otpravitel, dop_info):
    global map_number, config,tec_level
    if pismo == 'enemy_at_end':
        # print('E.A.E')
        enemys.remove(otpravitel)
        mainhp.hp_changing(dop_info)
    if pismo == 'bullet_letit':
        # print('B.A.P')
        for i in enemys:
            if i.get_rect().collidepoint(otpravitel.x, otpravitel.y):
                hp_System.HP_system.hp_changing(i.hp, -  otpravitel.damage)
                bullets.remove(otpravitel)
                break
    if pismo == 'bullet_at_pos':
        # print('B.A.P')
        bullets.remove(otpravitel)

    if pismo == 'death' and mainhp is otpravitel:        exit()

    if pismo == 'death':
        enemys.remove(dop_info)
        wallet.otnimanie(-15)
        if enemys == []:
            map_number += 1
            tec_level=try_to_load_config(map_number)
            if tec_level is None:
                exit()
f = open("levels/Tutorial.yaml", 'r', encoding="utf-8")
config = yaml.safe_load(f)

tec_level = level.Level(config['map'])

map_number = 0

wallet = wallet.get_wallet(100)

clock = pygame.time.Clock()

bullets = []
apple = None

y = 80

mainhp = tec_level.mainhp

magaz = shop.Magazin(803, 80, 'images/UI/TowerButtons/button_1.png', 35, poisontower.Poison_tower, vibor_bashni)
magaz2 = shop.Magazin(803, 190, 'images/UI/TowerButtons/button_2.png', 70, firetower.Fire_tower, vibor_bashni)
magaz3 = shop.Magazin(803, 300, 'images/UI/TowerButtons/button_3.png', 140, stormtower.Storm_tower, vibor_bashni)
magaz4 = shop.Magazin(803, 410, 'images/UI/TowerButtons/button_4.png', 240, icetower.Ice_tower, vibor_bashni)
bazar = [magaz, magaz2]

perecluthatel = False

enemys = []

messenger.messenger.podpisatsa(messages)
