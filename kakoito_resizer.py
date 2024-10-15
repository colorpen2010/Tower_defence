import pygame

def schoti():
    """
    считает игрик обьекта
    :return:
    """
    # igrik=
    pass
def creating_objects(pyt, map):
    """
    создаёт картинку нужного размера

    :param pyt:
    :return:
    """


    # x = round(800 / pixels, 0)
    kolithestwo_strok = len(map.split('\n'))

    cell_size = 800/kolithestwo_strok

    image = pygame.image.load(pyt)

    visota_imeiga = image.get_height()
    shirina_imeiga = image.get_width()

    visota_kartinki= visota_imeiga*cell_size/shirina_imeiga

    image = pygame.transform.scale(image, [cell_size,visota_kartinki])
    return image


map = """25342352
31001103
22543205
30110014
20453423
30110102
24534502
32342453"""
project=creating_objects('images/Towers/PoisonIdle/0.png', map)
pygame.image.save(project,'test/test_5.png')
