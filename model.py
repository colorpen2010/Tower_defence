import pygame
from pygame.examples.cursors import image

from classes import animator, enemy_factory, entity, tower_class,plitochniy_zavod

clock = pygame.time.Clock()

map = """25342352
31001103
22543205
30110014
20453423
30110102
24534502
32342453"""

# map="""02354
# 15344
# 04233
# 01322
# 20253"""
apple=tower_class.towernicsemus3_alhabethangerald3(map,'images/Towers/PoisonIdle/0.png')
korzina=[]
korzina.append(apple)

spisoc=[]

animated_red_portal= animator.Animator('images/Portal/Idle__/red_idle', 40, map)
# test_tower=kakoito_resizer.creating_objects('images/Towers/PoisonIdle/0.png')


tower = (pygame.image.load('images/Towers/PoisonIdle/0.png'))

animated_towers=[]

toweronisreximus2 = entity.generation(tower, types=1)
pixels_public = toweronisreximus2.resizer_part(map)
toweronisreximus2.resive(pixels_public)
# map_rect=pygame.rect.Rect()
kva = []
sbackground1 = pygame.image.load('images/Tiles/sand_01.png')
sbackground2 = pygame.image.load('images/Tiles/sand_02.png')
gbackground1 = pygame.image.load('images/Tiles/grass_01.png')
gbackground2 = pygame.image.load('images/Tiles/grass_02.png')
gbackground3 = pygame.image.load('images/Tiles/grass_03.png')
gbackground4 = pygame.image.load('images/Tiles/grass_04.png')

bpbackground5=pygame.surface.Surface([400,487],pygame.SRCALPHA)
blue_portal = pygame.image.load('images/Portal/Idle__/blue_idle/1.png')
blue_portalius2= entity.generation(blue_portal, types=1)
blue_portalius2.resive(pixels_public)

red_portal = pygame.image.load('images/Portal/Idle__/red_idle/01.png')

backgrounds = [sbackground1, sbackground2, gbackground1, gbackground2, gbackground3, gbackground4]


# plitka=plitochniy_zavod.Tsekh('sky',100,200,map)
# plitka2=plitochniy_zavod.Tsekh('grass',200,0,map)


bportal= entity.generation(blue_portal, types=1)
bportal.resive(pixels_public)
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
            # spisoc.append({'rect': rectik, 'type': 's', 'building': False})

        else:
            spisoc.append(plitochniy_zavod.Tsekh('grass',dest,height,map))
            # spisoc.append({'rect': rectik, 'type': 'g', 'building': False})
        if dest!=pygame.display.get_window_size()[0]-spisoc[-1].get_product_size()[0]:
            dest +=spisoc[-1].get_product_size()[0]
        else:
            dest=0
            height+=spisoc[-1].get_product_size()[1]
            # self.y=self.x

def ystanowka_bashni(pos):
    i=poisk_kletki(pos)
    if i.type == 'grass':
        i.building = 'tower'
        i.tower = tower_class.towernicsemus3_alhabethangerald3(map,'images/Towers/PoisonIdle/0.png')

def poisk_kletki(pos):
    for i in spisoc:
        rect=i.get_rect()
        if rect.collidepoint(pos):
            return i

map_regeneration(map)
# number=0
# for o in spisoc:
#     image=pygame.Surface([100,100])
#     o.okraska(image)
#     number+=1
    # pygame.image.save(image,'test/test_spisok'+str(number)+'.png')

regeneration = entity.generation(backgrounds, background=background)
regeneration.resive(pixels_public)
# regeneration.map_generation()
# regeneration.spisoc[9]['building']='blue_portal'
# regeneration.spisoc[54]['building']='red_portal'