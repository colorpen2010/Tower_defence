import pygame


def creating_objects(pyt, map, x=20,pixels=10):
    """
    создаёт картинку нужного размера
    :param pyt:
    :return:
    """

    # x = round(800 / pixels, 0)
    kolithestwo_strok = len(map.split('\n'))
    visota_pola = kolithestwo_strok * x

    image = pygame.image.load(pyt)
    image = pygame.transform.scale(image, [visota_pola,visota_pola+172/3])
    return image


map = """25342352
31001103
22543205
30110014
20453423
30110102
24534502
32342453"""
project=creating_objects('images/Tiles/wall.png', map)
pygame.image.save(project,'test/test_3.png')
