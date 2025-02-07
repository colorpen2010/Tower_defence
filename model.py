import pygame

from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop,wallet,firetower,poisontower,stormtower,icetower,\
    warehouse

# def razmer_plitki(nuber=0):
#     return plitki[-1].get_product_size()[nuber]


def map_regeneration(map):
    global house,animated_blue_portal,animated_red_portal

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
        if i == '\n':
            if len(etasch)!=0:
                house.append(etasch)
                etasch=[]
    razmer_plitki = 800 / (len(house))
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
                    route.append([dest + razmer_plitki / 2, height + razmer_plitki / 2, 0])
                elif shitel == ')':
                    kletka[0]='sand'
                    kletka.append(')')
                    route.append([dest + razmer_plitki / 2, height + razmer_plitki / 2, 999])
                elif shitel.isnumeric():
                    kletka[0]='sand'
                    route.append([dest + razmer_plitki / 2, height + razmer_plitki / 2, int(shitel)])




            plitki.append(plitochniy_zavod.Tsekh(kletka[0], kletka[1], kletka[2], kletka[3]))
            if kletka[-1]=='(':
                animated_blue_portal = animator.Animator('images/Portal/Idle__/blue_idle', 40, len(house), False, x=dest, bottom=height + height + razmer_plitki)
            if kletka[-1]==')':
                animated_red_portal = animator.Animator('images/Portal/Idle__/red_idle', 40, len(house), False, x=dest, bottom=height + razmer_plitki)

            if dest<pygame.display.get_window_size()[0]-razmer_plitki:
                dest +=razmer_plitki
            # else:
            # spisoc.append(plitochniy_zavod.Tsekh('grass',dest,height,map))

            else:
                dest=0
                height+=razmer_plitki
    print(len(plitki))
    route.sort(key=lambda element: element[2])
    for o in route:
        del o[-1]
        #     # self.y=self.x

def vibor_bashni(bashnia,shop):
    global apple
    i=poisk_kletki(pygame.mouse.get_pos())
    if shop.numprice<=wallet.money:
        apple=bashnia(i.x,i.get_rect().bottom)
        apple.shop=shop


def ystanowka_portala(nomer,type):
    with_portal=plitki[nomer]
    if type=='red':
        with_portal.building='red_portal'
    if type=='blue':
        with_portal.building='blue_portal'

def ystanowka_bashni(pos):
    global apple
    i=poisk_kletki(pos)
    if i.type == 'grass' and apple!=None and wallet.money>=apple.shop.numprice and i.building==None:
        wallet.otnimanie(apple.shop.numprice)
        i.building = 'tower'
        tyipiok=type(apple)
        i.tower=tyipiok(i.x,i.get_rect().bottom)
        if wallet.money<apple.shop.numprice:
            apple=None

def poisk_kletki(pos):
    for i in plitki:
        rect=i.get_rect()
        if rect.collidepoint(pos):
            return i

wallet=wallet.get_wallet(100 )

house = []



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

map= """
[(*][*4][**][51][+_]
[+_][+*][+_][+*][+_]
[+_][*3][+*][_2][+_]
[+_][+_][+_][)*][+_]
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
map_regeneration(map)



magaz=shop.Magazin(803,80,'images/UI/TowerButtons/button_1.png',35,poisontower.Poison_tower,vibor_bashni)
magaz2=shop.Magazin(803,190,'images/UI/TowerButtons/button_2.png',70,firetower.Fire_tower,vibor_bashni)
magaz3=shop.Magazin(803,300,'images/UI/TowerButtons/button_3.png',140,stormtower.Storm_tower,vibor_bashni)
magaz4=shop.Magazin(803,410,'images/UI/TowerButtons/button_4.png',240,icetower.Ice_tower,vibor_bashni)
bazar=[magaz,magaz2,magaz3,magaz4]




change = False

perecluthatel = False


xy = 50
# enemy1 = enemy_factory.enem_factory('blue', len(house), True, 0.5, scorost=1.50, spisok_tochek=route.copy())
# enemy2 = enemy_factory.enem_factory('purple', len(house), True, 1, scorost=0.50, spisok_tochek=route.copy(), bottom=200)
enemy3 = enemy_factory.enem_factory('green', len(house), True, [1,1,0.5,0.5], scorost=1.25, spisok_tochek=route.copy())
# enemy4 = enemy_factory.enem_factory('red', len(house), True, 0.9, scorost=0.80, spisok_tochek=route.copy(), bottom=200)

# enemy2 = enemy_factory.enem_factory('images/Monsters/move/purple_left/00.png',map,True,1,scorost=1,spisok_tochek=spisok_tochek.copy(),bottom=200)
# enemys=[enemy1,enemy2,enemy3,enemy4]
enemys=[enemy3]


background = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)



# ystanowka_portala(26,'red')
# ystanowka_portala(2,'blue')