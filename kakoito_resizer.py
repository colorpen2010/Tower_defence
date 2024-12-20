import pygame

def sheti(money):
    output=str(money)
    if money > 999 and money < 999999:
        output = str(round(money / 1000, 1)) + 'K'
    elif money > 999999 and money < 999999999:
        output = str(round(money / 1000000, 1)) + 'M'
    return output

def creating_objects_x(pyt, map, procent=1):
    """
    создаёт картинку нужного размера

    :param pyt:
    :return:
    """


    # x = round(800 / pixels, 0)
    kolithestwo_strok = len(map.split('\n'))

    cell_size = 800/(kolithestwo_strok/procent)

    image = pygame.image.load(pyt)

    visota_imeiga = image.get_height()
    shirina_imeiga = image.get_width()

    visota_kartinki= visota_imeiga*cell_size/shirina_imeiga

    image = pygame.transform.scale(image, [cell_size,visota_kartinki])
    return image

def creating_objects_y(pyt, map,procent=1):
    """
    создаёт картинку нужного размера

    :param pyt:
    :return:
    """


    # x = round(800 / pixels, 0)
    kolithestwo_strok = len(map.split('\n'))

    cell_size = 800/(kolithestwo_strok/procent)

    image = pygame.image.load(pyt)

    visota_imeiga = image.get_height()
    shirina_imeiga = image.get_width()

    shirina_kartinki= cell_size*shirina_imeiga/visota_imeiga

    image = pygame.transform.scale(image, [shirina_kartinki,cell_size])
    return image


map = """25342352
31001103
22543205
30110014
20453423
30110102
24534502
32342453"""
project=creating_objects_x('images/Towers/PoisonIdle/0.png', map)
# pygame.image.save(project,'test/test_5.png')
