import pygame

def sheti(money):
    output=str(money)
    if money > 999 and money < 999999:
        output = str(round(money / 1000, 1)) + 'K'
    elif money > 999999 and money < 999999999:
        output = str(round(money / 1000000, 1)) + 'M'
    return output

def creating_objects_x(pyt, kolithestvo_etashei, procent=1):
    """
    создаёт картинку нужного размера

    :param pyt:
    :return:
    """


    # x = round(800 / pixels, 0)


    cell_size = 800/(kolithestvo_etashei/procent)

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
    kolithestwo_strok = map

    cell_size = 800/(kolithestwo_strok/procent)

    image = pygame.image.load(pyt)

    visota_imeiga = image.get_height()
    shirina_imeiga = image.get_width()

    shirina_kartinki= cell_size*shirina_imeiga/visota_imeiga

    image = pygame.transform.scale(image, [shirina_kartinki,cell_size])
    return image


# pygame.image.save(project,'test/test_5.png')
