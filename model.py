import pygame, math_utils, yaml, os

from classes import hp_System, enemy_factory, shop, firetower, poisontower, \
    stormtower, icetower, messenger, level, portal,wave,buttons,timer_launcher,\
    button_with_layers



def vibor_bashni(bashnia, shop):
    global apple
    i = tec_level.poisk_kletki(pygame.mouse.get_pos())
    if shop.numprice <= tec_level.wallet.money:
        if apple is not None:
            apple.kill_me()
        apple = bashnia(i.x, i.get_rect().bottom, tec_level.give_your_number_of_etashey(), True)
        apple.shop = shop


def ystanowka_bashni(pos):
    global apple
    i = tec_level.poisk_kletki(pos)
    if i.type == 'grass' and apple != None and tec_level.wallet.money >= apple.shop.numprice and i.building == None:
        tec_level.wallet.otnimanie(apple.shop.numprice)
        i.building = 'tower'
        tyipiok = type(apple)
        i.tower = tyipiok(i.x, i.get_rect().bottom, tec_level.give_your_number_of_etashey())
        if tec_level.wallet.money < apple.shop.numprice:
            apple.kill_me()
            apple = None




def try_to_load_config(number):
    if os.path.exists("levels/map_" + str(number) + ".yaml"):
        f = open("levels/map_" + str(map_number) + ".yaml", 'r', encoding="utf-8")
        config = yaml.safe_load(f)
        # print(config)
        tec_level=level.Level(config['map'])
        tec_wave = wave.Wave(tec_level, config['types'])
        return tec_level,tec_wave
    else:
        return None

def messages(pismo, otpravitel, dop_info):
    global map_number, config,tec_level,tec_wave,apple
        # print('B.A.P')



    if pismo == 'death' and mainhp is otpravitel:        exit()


    if pismo == 'wave_no_enemys':
        map_number += 1
        resultat=try_to_load_config(map_number)
        if apple is not None:
            apple.kill_me()
            apple = None
        if resultat!= None:
            tec_level, tec_wave=resultat
        else:
            exit()






f = open("levels/Tutorial.yaml", 'r', encoding="utf-8")
config = yaml.safe_load(f)

tec_level = level.Level(config['map'])

tec_wave=wave.Wave(tec_level, config['types'])

map_number = 0


clock = pygame.time.Clock()
apple = None

normal=buttons.Knopka(50,50,"images/UI/speedup/1.png",timer_launcher.timer_worker.timers_change,dop_info={"milisec": 10})
speed=buttons.Knopka(50,50,"images/UI/speedup/2.png",timer_launcher.timer_worker.timers_change,dop_info={"milisec": 30})
super_speed=buttons.Knopka(50,50,"images/UI/speedup/4.png",timer_launcher.timer_worker.timers_change,dop_info={"milisec": 60})

time_button=button_with_layers.Button_with_layers([normal,speed,super_speed])


y = 80

mainhp = tec_level.mainhp

magaz = shop.Magazin(803, 80, 'images/UI/TowerButtons/button_1.png', 35, poisontower.Poison_tower, vibor_bashni)
magaz2 = shop.Magazin(803, 190, 'images/UI/TowerButtons/button_2.png', 100, firetower.Fire_tower, vibor_bashni)
magaz3 = shop.Magazin(803, 300, 'images/UI/TowerButtons/button_3.png', 135, stormtower.Storm_tower, vibor_bashni)
magaz4 = shop.Magazin(803, 410, 'images/UI/TowerButtons/button_4.png', 235, icetower.Ice_tower, vibor_bashni)
bazar = [magaz, magaz2]

perecluthatel = False


messenger.messenger.podpisatsa(messages)
# blue=enemy_creating('blue',1,True)
# green=enemy_creating('green',2,True)
# blue_portal=portal.Portal('start',10,5,12+3)
# red_portal=portal.Portal('finish',10,2,5+4)
# objects=[blue,green,blue_portal,red_portal]
# print(math_utils.sravnivatel(blue_portal,[],blue,tec_level)==1)
# print(math_utils.sravnivatel(blue_portal,[],green,tec_level)==1)
# print(math_utils.sravnivatel(red_portal,[],blue,tec_level)==1)