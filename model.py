import pygame,math_utils,yaml,os

from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop,wallet,firetower,poisontower,stormtower,icetower,\
    warehouse,messenger,hp_System,level

tutorial_level=level.Level()
# def razmer_plitki(nuber=0):
#     return plitki[-1].get_product_size()[nuber]
f=open("levels/Tutorial.yaml", 'r', encoding="utf-8")
config=yaml.safe_load(f)
print(config)
level=0

def vibor_bashni(bashnia,shop):
    global apple
    i=math_utils.poisk_kletki(pygame.mouse.get_pos(),tutorial_level.plitki)
    if shop.numprice<=wallet.money:
        apple=bashnia(i.x,i.get_rect().bottom,True)
        apple.shop=shop


def ystanowka_portala(nomer,type):
    with_portal=tutorial_level.plitki[nomer]
    if type=='red':
        with_portal.building='red_portal'
    if type=='blue':
        with_portal.building='blue_portal'

def ystanowka_bashni(pos):
    global apple
    i=math_utils.poisk_kletki(pos,tutorial_level.plitki)
    if i.type == 'grass' and apple!=None and wallet.money>=apple.shop.numprice and i.building==None:
        wallet.otnimanie(apple.shop.numprice)
        i.building = 'tower'
        tyipiok=type(apple)
        i.tower=tyipiok(i.x,i.get_rect().bottom)
        if wallet.money<apple.shop.numprice:
            apple=None


wallet=wallet.get_wallet(100 )

house = []

clock = pygame.time.Clock()

test_map_ver1= """
[+_][+_][+_][+_][+_][*+]
[(*][51][*+][62][+_][*+]
[+_][*+][+_][*+][+_][*+]
[+_][*4][*+][73][)+][*+]
[+_][+_][+_][+_][+_][*+]
"""

test_map_ver2="""
[+_][+_][+_][+_][+_][*+]
[(*][*+][)+][+_][+_][*+]
[+_][+_][+_][+_][+_][*+]
[+_][+_][+_][+_][+_][*+]
[+_][+_][+_][+_][+_][*+]
"""

tutorial_map= """
[(*][1+][+_][4+][*+][5+][+_][*+]
[+_][*+][+_][*+][+_][*+][+_][*+]
[+_][*+][+_][*+][+_][*+][+_][*+]
[+_][*+][+_][*+][+_][*+][+_][*+]
[+_][*+][+_][*+][+_][*+][+_][*+]
[+_][*+][+_][*+][+_][*+][+_][*+]
[+_][2+][*+][3+][+_][6+][)*][*+]
"""

') выход'
'( вход'
'_ трава'
'+ ничего'
'* песок'



map= """
[+_][+_][+_][+_][+_][*+]
[(*][51][*+][62][+_][*+]
[+_][*+][+_][*+][+_][*+]
[+_][*4][*+][73][)+][*+]
[+_][+_][+_][+_][+_][*+]
"""







fly=False

# map="""023540
# 153440
# 042330
# 013220
# 202530"""

bullets=[]
apple=None

korzina=[]
korzina.append(apple)



y=80


tutorial_level.map_generation(config['map'])


magaz=shop.Magazin(803,80,'images/UI/TowerButtons/button_1.png',35,poisontower.Poison_tower,vibor_bashni)
magaz2=shop.Magazin(803,190,'images/UI/TowerButtons/button_2.png',70,firetower.Fire_tower,vibor_bashni)
magaz3=shop.Magazin(803,300,'images/UI/TowerButtons/button_3.png',140,stormtower.Storm_tower,vibor_bashni)
magaz4=shop.Magazin(803,410,'images/UI/TowerButtons/button_4.png',240,icetower.Ice_tower,vibor_bashni)
bazar=[magaz,magaz2]




change = False

perecluthatel = False


# xy = 50

enemys=[]
def enemy_creating(type,hp):
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
    if type=='blue':
        enemy = enemy_factory.enem_factory(type, len(house), True, [0.5, 0.5, 0.5, 0.5], scorost=2.45,
                                            spisok_tochek=tutorial_level.route.copy(),damage=-5,hp=hp)
    elif type=='purple':
        enemy = enemy_factory.enem_factory(type, len(house), True, [1, 1, 1, 1], scorost=0.50,
                                            spisok_tochek=tutorial_level.route.copy(),damage=-20,hp=hp)
    elif type=='green':
        enemy = enemy_factory.enem_factory(type, len(house), True, [1, 1, 0.5, 0.5], scorost=1.50,
                                            spisok_tochek=tutorial_level.route.copy(),damage=-10,hp=hp)
    elif type=='red':
        enemy = enemy_factory.enem_factory(type, len(house), True, [0.8, 0.8, 0.8, 0.8], scorost=0.8,
                                            spisok_tochek=tutorial_level.route.copy(),damage=-15,hp=hp)
    if enemy!=None:
        enemys.append(enemy)



# enemy2 = enemy_factory.enem_factory('images/Monsters/move/purple_left/00.png',map,True,1,scorost=1,spisok_tochek=spisok_tochek.copy(),bottom=200)


def messages(pismo, otpravitel, dop_info):
    global level,config
    if pismo=='enemy_at_end':
        # print('E.A.E')
        enemys.remove(otpravitel)
        mainhp.hp_changing(dop_info)
    if pismo=='bullet_letit':
        # print('B.A.P')
        for i in enemys:
            if i.get_rect().collidepoint(otpravitel.x,otpravitel.y):
                hp_System.HP_system.hp_changing(i.hp,-  otpravitel.damage)
                bullets.remove(otpravitel)
                break
    if pismo=='bullet_at_pos':
        # print('B.A.P')
        bullets.remove(otpravitel)
    if pismo=='death':
        if mainhp is otpravitel:
            exit()
        else:
            enemys.remove(dop_info)
            if enemys==[]:
                if os.path.exists("levels/map_"+str(level+1)+".yaml"):
                    level += 1
                else:
                    exit()
                if os.path.exists("levels/map_"+str(level)+".yaml"):
                    f = open("levels/map_"+str(level)+".yaml", 'r', encoding="utf-8")
                    config = yaml.safe_load(f)
                    print(config)
                    wallet.set_money(100)
                    wallet.otnimanie(-100)
                    mainhp.hp_changing(mainhp.max_hp-mainhp.tec_hp)
                    tutorial_level.map_generation(config['map'])
            wallet.otnimanie(-7)


messenger.messenger.podpisatsa(messages)

background = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)



# ystanowka_portala(26,'red')
# ystanowka_portala(2,'blue')