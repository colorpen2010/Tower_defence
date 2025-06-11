import pygame

def sheti(money):
    output=str(money)
    if money > 999 and money < 999999:
        output = str(round(money / 1000, 1)) + 'K'
    elif money > 999999 and money < 999999999:
        output = str(round(money / 1000000, 1)) + 'M'
    return output

def cell_size_giver(kolithestvo_etashei, procent=1):

    return 800/(kolithestvo_etashei)*procent


def check_pixel_collision(image1, pos1, image2, pos2):
    """
    Проверяет, пересекаются ли непрозрачные пиксели двух изображений.

    :param image1: Surface первого изображения
    :param pos1: (x, y) позиция первого изображения на экране
    :param image2: Surface второго изображения
    :param pos2: (x, y) позиция второго изображения на экране
    :return: True, если пересекаются хотя бы одним непрозрачным пикселем, иначе False
    """
    mask1 = pygame.mask.from_surface(image1)
    mask2 = pygame.mask.from_surface(image2)

    offset_x = pos2[0] - pos1[0]
    offset_y = pos2[1] - pos1[1]

    overlap_point = mask1.overlap(mask2, (offset_x, offset_y))

    return overlap_point is not None

def sprites_collide(sprite1, sprite2):

    res = pygame.sprite.collide_mask(sprite1, sprite2)
    if not res:
        return False

    res = [*res]
    res[0] += sprite1.rect.left
    res[1] += sprite1.rect.top
    return res

def creating_objects_x(pyt, kolithestvo_etashei, procent=1):
    """
    создаёт картинку нужного размера

    :param pyt:
    :return:
    """

    cell_size=cell_size_giver(kolithestvo_etashei,procent)
    # x = round(800 / pixels, 0)



    image = pygame.image.load(pyt)

    visota_imeiga = image.get_height()
    shirina_imeiga = image.get_width()

    visota_kartinki= visota_imeiga*cell_size/shirina_imeiga

    image = pygame.transform.scale(image, [cell_size,visota_kartinki])
    return image

# def creating_objects_y(pyt, map,procent=1):
#     """
#     создаёт картинку нужного размера
#
#     :param pyt:
#     :return:
#     """
#
#
#     # x = round(800 / pixels, 0)
#     kolithestwo_strok = map
#
#     cell_size = 800/(kolithestwo_strok/procent)
#
#     image = pygame.image.load(pyt)
#
#     visota_imeiga = image.get_height()
#     shirina_imeiga = image.get_width()
#
#     shirina_kartinki= cell_size*shirina_imeiga/visota_imeiga
#
#     image = pygame.transform.scale(image, [shirina_kartinki,cell_size])
#     return image


# pygame.image.save(project,'test/test_5.png')
