import os

import pygame, entity, enemy_factory,animator,kakoito_resizer

import image_worker

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

spisok = []
file_list=os.listdir('images/Portal/Idle__/red_idle')
for p in file_list:
    spisok.append('images/Portal/Idle__/red_idle/'+p)
animation= animator.Animator(spisok,50)

test_tower=kakoito_resizer.creating_objects('images/Towers/PoisonIdle/0.png')

tower = (pygame.image.load('images/Towers/PoisonIdle/0.png'))
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
blue_portalius2=entity.generation(blue_portal,types=1)
blue_portalius2.resive(pixels_public)

red_portal = pygame.image.load('images/Portal/Idle__/red_idle/01.png')
red_portaliuinus2=entity.generation(red_portal,types=1)
red_portaliuinus2.resive(pixels_public)

backgrounds = [sbackground1, sbackground2, gbackground1, gbackground2, gbackground3, gbackground4]

bportal=entity.generation(blue_portal,types=1)
bportal.resive(pixels_public)
change = False

perecluthatel = False

xy = 50
enemy1 = enemy_factory.enem_factory(pygame.image.load('images/Monsters/move/blue_right.png'))
imaging = pygame.Surface([220, 320], pygame.SRCALPHA)
imaging.blit(enemy1.enemy, [0, 0], [20, 15, 246, 320])
imaging = pygame.transform.scale(imaging, [220 / 7, 320 / 7])

background = pygame.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)

def ystanowka_bashni(pos):
    i=poisk_kletki(pos)
    if i[1] == 'g':
        i[2] = 'tower'
def poisk_kletki(pos):
    for i in regeneration.spisoc:
        if i[0].collidepoint(pos):
            return i

regeneration = entity.generation(backgrounds, background=background)
regeneration.resive(pixels_public)
regeneration.map_regeneration(map, backgrounds)
print('a')
# regeneration.map_generation()
regeneration.spisoc[9][2]='blue_portal'
regeneration.spisoc[54][2]='red_portal'