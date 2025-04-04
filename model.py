import pygame,math_utils,yaml

from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop,wallet,firetower,poisontower,stormtower,icetower,\
    warehouse,messenger,hp_System

# def razmer_plitki(nuber=0):
#     return plitki[-1].get_product_size()[nuber]
f=open("config.yaml",'r',encoding="utf-8")
config=yaml.safe_load(f)
print(config)
def map_regeneration(map):
    global house,animated_blue_portal,animated_red_portal,mainhp

    switch = False
    door = []
    etasch = []


    height = 0
    dest = height

    for i in map:
        if i == '[' or switch==True:
            switch=True
            if i==']':
                switch=False
                etasch.append(door)
                door=[]
            elif i!='[':
                door.append(i)
        if i == ' ':
            if len(etasch)!=0:
                house.append(etasch)
                etasch=[]
    razmer_plitki = 800 // (len(house))
    for etasch in house:
        for door in etasch:
            kletka=['sand', dest, height, len(house)]
            for shitel in door:
                if shitel == '*':
                    kletka[0]='sand'
                elif shitel == '_':
                    kletka[0]='grass'
                elif shitel == '(':
                    kletka[0]='sand'
                    kletka.append('(')
                    route.append([int(dest + razmer_plitki / 2), int(height + razmer_plitki / 2), 0])
                elif shitel == ')':
                    kletka[0]='sand'
                    kletka.append(')')
                    route.append([int(dest + razmer_plitki / 2), int(height + razmer_plitki / 2), 999])
                elif shitel.isnumeric():
                    kletka[0]='sand'
                    route.append([int(dest + razmer_plitki / 2), int(height + razmer_plitki / 2), int(shitel)])




            plitki.append(plitochniy_zavod.Tsekh(kletka[0], kletka[1], kletka[2], kletka[3]))
            if kletka[-1]=='(':
                animated_blue_portal = animator.Animator('images/Portal/Idle__/blue_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)
            if kletka[-1]==')':
                animated_red_portal = animator.Animator('images/Portal/Idle__/red_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)
                mainhp.centerx=animated_red_portal.get_center()[0]
                mainhp.bottom=animated_red_portal.get_rect()[1]
            if dest<pygame.display.get_window_size()[0]-razmer_plitki:
                dest +=razmer_plitki
            # else:
            # spisoc.append(plitochniy_zavod.Tsekh('grass',dest,height,map))

            else:
                dest=0
                height+=razmer_plitki
    route.sort(key=lambda element: element[2])
    for o in route:
        del o[-1]
        #     # self.y=self.x

def vibor_bashni(bashnia,shop):
    global apple
    i=math_utils.poisk_kletki(pygame.mouse.get_pos(),plitki)
    if shop.numprice<=wallet.money:
        apple=bashnia(i.x,i.get_rect().bottom,True)
        apple.shop=shop


def ystanowka_portala(nomer,type):
    with_portal=plitki[nomer]
    if type=='red':
        with_portal.building='red_portal'
    if type=='blue':
        with_portal.building='blue_portal'

def ystanowka_bashni(pos):
    global apple
    i=math_utils.poisk_kletki(pos,plitki)
    if i.type == 'grass' and apple!=None and wallet.money>=apple.shop.numprice and i.building==None:
        wallet.otnimanie(apple.shop.numprice)
        i.building = 'tower'
        tyipiok=type(apple)
        i.tower=tyipiok(i.x,i.get_rect().bottom)
        if wallet.money<apple.shop.numprice:
            apple=None


wallet=wallet.get_wallet(100 )

house = []

mainhp=hp_System.HP_system(300,152,500,500,100,30)
clock = pygame.time.Clock()

map = """253423520
310011030
225432050
301100140
204534230
301101020
245345020
323424530"""
# map2 = """430320
# 341230
# 430320
# 231530
# 430230"""

future_map_idea_1= """
_______*
_(***1_*
_4***5_*
_**_76_*
_39*82_*
_*a**)_*
_______*"""

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

plitki=[]

route=[]

y=80

animated_blue_portal=None
animated_red_portal=None
map_regeneration(config['map'])


magaz=shop.Magazin(803,80,'images/UI/TowerButtons/button_1.png',35,poisontower.Poison_tower,vibor_bashni)
magaz2=shop.Magazin(803,190,'images/UI/TowerButtons/button_2.png',70,firetower.Fire_tower,vibor_bashni)
magaz3=shop.Magazin(803,300,'images/UI/TowerButtons/button_3.png',140,stormtower.Storm_tower,vibor_bashni)
magaz4=shop.Magazin(803,410,'images/UI/TowerButtons/button_4.png',240,icetower.Ice_tower,vibor_bashni)
bazar=[magaz,magaz2]




change = False

perecluthatel = False


# xy = 50

enemys=[]
def enemy_creating(type):
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
                                            spisok_tochek=route.copy(),damage=-5,hp=2)
    elif type=='purple':
        enemy = enemy_factory.enem_factory(type, len(house), True, [1, 1, 1, 1], scorost=0.50,
                                            spisok_tochek=route.copy(),damage=-20,hp=100)
    elif type=='green':
        enemy = enemy_factory.enem_factory(type, len(house), True, [1, 1, 0.5, 0.5], scorost=1.50,
                                            spisok_tochek=route.copy(),damage=-10,hp=4)
    elif type=='red':
        enemy = enemy_factory.enem_factory(type, len(house), True, [0.8, 0.8, 0.8, 0.8], scorost=0.8,
                                            spisok_tochek=route.copy(),damage=-15,hp=100)
    if enemy!=None:
        enemys.append(enemy)



# enemy2 = enemy_factory.enem_factory('images/Monsters/move/purple_left/00.png',map,True,1,scorost=1,spisok_tochek=spisok_tochek.copy(),bottom=200)


def messages(pismo, otpravitel, dop_info):
    if pismo=='enemy_at_end':
        # print('E.A.E')
        enemys.remove(otpravitel)
        mainhp.hp_changing(dop_info)
    if pismo=='bullet_letit':
        # print('B.A.P')
        for i in enemys:
            if i.get_rect().collidepoint(otpravitel.x,otpravitel.y):
                wallet.otnimanie(-7)
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
messenger.messenger.podpisatsa(messages)

background = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)



# ystanowka_portala(26,'red')
# ystanowka_portala(2,'blue')