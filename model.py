import pygame,entity,enemy_factory
# map_rect=pygame.rect.Rect()
kva=[]
sbackground1=pygame.image.load('images/Tiles/sand_01.png')
sbackground2=pygame.image.load('images/Tiles/sand_02.png')
gbackground1=pygame.image.load('images/Tiles/grass_01.png')
gbackground2=pygame.image.load('images/Tiles/grass_02.png')
gbackground3=pygame.image.load('images/Tiles/grass_03.png')
gbackground4=pygame.image.load('images/Tiles/grass_04.png')
backgrounds=[sbackground1,sbackground2,gbackground1,gbackground2,gbackground3,gbackground4]

perecluthatel=False

xy=50
enemy1=enemy_factory.enem_factory(pygame.image.load('images/Monsters/move/blue_ right.png'))
imaging=pygame.Surface([220,320],pygame.SRCALPHA)
imaging.blit(enemy1.enemy,[0,0],[20,15,246,320])
imaging=pygame. transform.scale(imaging,[220/7,320/7])

background=pygame.Surface(pygame.display.get_window_size(),pygame.SRCALPHA)

regeneration=entity.generation(background,backgrounds)

regeneration.resize_randomizer()
regeneration.resive(kva)
regeneration.map_generation()
