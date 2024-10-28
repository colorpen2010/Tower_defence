import pygame
from pygame.examples.cursors import image

from classes import animator, enemy_factory, tower_class,plitochniy_zavod,shop

clock = pygame.time.Clock()

map = """253423520
310011030
225432050
301100140
204534230
301101020
245345020
323424530"""

# map="""02354
# 15344
# 04233
# 01322
# 20253"""
apple=tower_class.towernicsemus3_alhabethangerald3(map,'images/Towers/PoisonIdle/0.png')
korzina=[]
korzina.append(apple)

spisoc=[]

magaz=shop.Magazin(803,80,'images/UI/TowerButtons/button_1.png',213419999)
magaz2=shop.Magazin(803,190,'images/UI/TowerButtons/button_2.png',213412)
magaz3=shop.Magazin(803,300,'images/UI/TowerButtons/button_3.png',2112)
magaz4=shop.Magazin(803,410,'images/UI/TowerButtons/button_4.png',21342)


animated_blue_portal= animator.Animator('images/Portal/Idle__/blue_idle', 40, map,False)
animated_red_portal= animator.Animator('images/Portal/Idle__/red_idle', 40, map,False)

change = False

perecluthatel = False

xy = 50
enemy1 = enemy_factory.enem_factory(pygame.image.load('images/Monsters/move/blue_right.png'))
imaging = pygame.Surface([220, 320], pygame.SRCALPHA)
imaging.blit(enemy1.enemy, [0, 0], [20, 15, 246, 320])
imaging = pygame.transform.scale(imaging, [220 / 7, 320 / 7])

background = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)

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
        if dest!=pygame.display.get_window_size()[0]-spisoc[-1].get_product_size()[0]:
            dest +=spisoc[-1].get_product_size()[0]
        else:
            dest=0
            height+=spisoc[-1].get_product_size()[1]
            # self.y=self.x

def ystanowka_portala(nomer,type):
    with_portal=spisoc[nomer]
    if type=='red':
        with_portal.building='red_portal'
    if type=='blue':
        with_portal.building='blue_portal'

def ystanowka_bashni(pos):
    i=poisk_kletki(pos)
    if i.type == 'grass':
        i.building = 'tower'
        i.tower = tower_class.towernicsemus3_alhabethangerald3(map,'images/Towers/IceIdle_cleared/00.png')

def poisk_kletki(pos):
    for i in spisoc:
        rect=i.get_rect()
        if rect.collidepoint(pos):
            return i

map_regeneration(map)
ystanowka_portala(54,'red')
ystanowka_portala(9,'blue')