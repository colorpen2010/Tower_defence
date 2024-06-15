import pygame
# map_rect=pygame.rect.Rect()
kva=[]
sbackground1=pygame.image.load('images/Tiles/sand_01.png')
sbackground2=pygame.image.load('images/Tiles/sand_02.png')
gbackground1=pygame.image.load('images/Tiles/grass_01.png')
gbackground2=pygame.image.load('images/Tiles/grass_02.png')
gbackground3=pygame.image.load('images/Tiles/grass_03.png')
gbackground4=pygame.image.load('images/Tiles/grass_04.png')
backgrounds=[sbackground1,sbackground2,gbackground1,gbackground2,gbackground3,gbackground4]

for o in backgrounds:
    kva.append(pygame.transform.scale(o, [50, 50]))
backgrounds.clear()
for i in kva:
    backgrounds.append(i)
