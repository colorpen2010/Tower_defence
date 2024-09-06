import pygame

def creating_objects (pyt,map):
    """
    создаёт картинку нужного размера
    :param pyt:
    :return:
    """
    kolithestwo_strok=len(map.split('\n'))
    image=pygame.image.load(pyt)
    image=pygame.transform.scale(image,cell_size)
    return image


pygame.image.save(creating_objects('images/Tiles/wall.png',[400/2,572/2]),'test/test_2.png')
