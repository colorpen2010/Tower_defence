import pygame

from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop,wallet,firetower,poisontower,stormtower,icetower,\
    warehouse


def map_regeneration(map):
    height = 0
    dest = height
    for i in map:
        if i=='\n':
            continue
        if i == '0' or i == '1':
            spisoc.append(plitochniy_zavod.Tsekh('sand',dest,height,map))

        else:
            spisoc.append(plitochniy_zavod.Tsekh('grass',dest,height,map))
            # spisoc.append({'rect': rectik, 'type': 'g', 'building': False})
        if dest<pygame.display.get_window_size()[0]-spisoc[-1].get_product_size()[0]:
            dest +=spisoc[-1].get_product_size()[0]
        else:
            dest=0
            height+=spisoc[-1].get_product_size()[1]
            # self.y=self.x

def vibor_bashni(bashnia,shop):
    global apple
    i=poisk_kletki(pygame.mouse.get_pos())
    if shop.numprice<=wallet.money:
        apple=bashnia(i.x,i.get_rect().bottom)
        apple.shop=shop


def ystanowka_portala(nomer,type):
    with_portal=spisoc[nomer]
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
    for i in spisoc:
        rect=i.get_rect()
        if rect.collidepoint(pos):
            return i

wallet=wallet.get_wallet(100 )

clock = pygame.time.Clock()

map = """253423520
310011030
225432050
301100140
204534230
301101020
245345020
323424530"""

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

spisoc=[]

y=80

magaz=shop.Magazin(803,80,'images/UI/TowerButtons/button_1.png',35,poisontower.Poison_tower,vibor_bashni)
magaz2=shop.Magazin(803,190,'images/UI/TowerButtons/button_2.png',70,firetower.Fire_tower,vibor_bashni)
magaz3=shop.Magazin(803,300,'images/UI/TowerButtons/button_3.png',140,stormtower.Storm_tower,vibor_bashni)
magaz4=shop.Magazin(803,410,'images/UI/TowerButtons/button_4.png',240,icetower.Ice_tower,vibor_bashni)
bazar=[magaz,magaz2,magaz3,magaz4]


animated_blue_portal= animator.Animator('images/Portal/Idle__/blue_idle', 40, map,False)
animated_red_portal= animator.Animator('images/Portal/Idle__/red_idle', 40, map,False)

change = False

perecluthatel = False

spisok_tochek=[[650,150],[650,350],[150,350],[150,550],[650,550]]

xy = 50
enemy1 = enemy_factory.enem_factory('images/Monsters/move/blue_left/00.png',map,True,0.5,spisok_tochek=spisok_tochek.copy())
enemy2 = enemy_factory.enem_factory('images/Monsters/move/purple_left/00.png',map,True,1,scorost=1,spisok_tochek=spisok_tochek.copy(),bottom=200)
enemys=[enemy1,enemy2]


background = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)



map_regeneration(map)
ystanowka_portala(60,'red')
ystanowka_portala(10,'blue')