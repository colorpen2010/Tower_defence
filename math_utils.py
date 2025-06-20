import math,classes



def get_obj_type(obj):
    if isinstance(obj, classes.portal.Portal):
        t="P"
        bottom = obj.bottom
        rect = obj.get_rect()
    elif isinstance(obj,classes.tower_class.towernicsemus3_alhabethangerald3):
        t="T"
        bottom = obj.bottom
        rect = obj.get_rect()
    elif type(obj) == classes.enemy_factory.enem_factory:
        t="E"
        bottom = obj.enemy.bottom
        rect = obj.enemy.get_rect()
    return t, bottom, rect

def sravnivatel(first,kletki,second,level):
    first_type, first_bottom, first_rect=get_obj_type(first)
    second_type, second_bottom, second_rect = get_obj_type(second)
    collide = first_rect.colliderect(second_rect)


    if collide and first_type=="E" and second_type=="P":
        return -1
    elif collide and first_type=="P" and second_type=="E":
        return 1

    if first_bottom>second_bottom:
        return -1
    elif first_bottom==second_bottom:
        return 0
    elif first_bottom<second_bottom:
        return 1

    if isinstance(first,classes.portal.Portal):
        bottom=first.bottom

    elif isinstance(first,classes.tower_class.towernicsemus3_alhabethangerald3):
        bottom=first.bottom
    elif type(first)==classes.enemy_factory.enem_factory:
        bottom=first.enemy.bottom
    if isinstance(second,classes.portal.Portal):
        bottom2=second.bottom

    elif isinstance(second,classes.tower_class.towernicsemus3_alhabethangerald3):
        bottom2=second.bottom
    elif type(second)==classes.enemy_factory.enem_factory:
        bottom2=second.enemy.bottom

    if type(first) == classes.enemy_factory.enem_factory and isinstance(second , classes.portal.Portal):
            return -1
    if isinstance(first , classes.portal.Portal) and type(second) == classes.enemy_factory.enem_factory:
        return 1

    elif bottom>bottom2:
        return -1
    elif bottom==bottom2:
        return 0
    elif bottom<bottom2:
        return 1

def sortirovka(spisok,kletki,level,sravnivatel=sravnivatel):
    while True:
        worked = False
        for i in range(0,len(spisok)-1,1):
            # print(type(spisok[i]),type(spisok[i+1]),sravnivatel(spisok[i],kletki, spisok[i+1],level))
            if sravnivatel(spisok[i],kletki, spisok[i+1],level)==-1:
                worked=True
                spisok[i],spisok[i+1]=spisok[i+1],spisok[i]
        if worked==False:
            return spisok

def get_point_on_circle_right_bottom(center, start_point, angle_degrees):
    dx = start_point[0] - center[0]
    dy = start_point[1] - center[1]

    if dx == 0:
        b_degr = 90
    else:
        tanb = dy / dx
        b_degr = math.degrees(math.atan(tanb))

    c_degr = 90 - b_degr + angle_degrees / 2

    hip = math.hypot(dx, dy)
    l = 2 * hip * math.sin(math.radians(angle_degrees / 2))

    dx = l * math.cos(math.radians(c_degr))
    dy = -l * math.sin(math.radians(c_degr))

    return [dx, dy]

def get_point_on_circle_right_top(center, start_point, angle_degrees):
    dx = start_point[0] - center[0]
    dy = center[1] - start_point[1]

    if dy == 0:
        b_degr = 90
    else:
        tanb = dx / dy
        b_degr = math.degrees(math.atan(tanb))

    c_degr = 90 - b_degr + angle_degrees / 2

    hip = math.hypot(dx, dy)
    l = 2 * hip * math.sin(math.radians(angle_degrees / 2))

    dx = -l * math.sin(math.radians(c_degr))
    dy = -l * math.cos(math.radians(c_degr))

    return [dx, dy]


def get_point_on_circle_left_top(center, start_point, angle_degrees):
    dx = center[0] - start_point[0]
    dy = center[1] - start_point[1]

    if dx == 0:
        b_degr = 90
    else:
        tanb = dy / dx
        b_degr = math.degrees(math.atan(tanb))

    c_degr = 90 - b_degr + angle_degrees / 2

    hip = math.hypot(dx, dy)
    l = 2 * hip * math.sin(math.radians(angle_degrees / 2))

    dx = -l * math.cos(math.radians(c_degr))
    dy = l * math.sin(math.radians(c_degr))

    return [dx, dy]

def get_point_on_circle_left_bottom(center, start_point, angle_degrees):
    dx = center[0] - start_point[0]
    dy = start_point[1] - center[1]

    if dy == 0:
        b_degr = 90
    else:
        tanb = dx / dy
        b_degr = math.degrees(math.atan(tanb))

    c_degr = 90 - b_degr + angle_degrees / 2

    hip = math.hypot(dx, dy)
    l = 2 * hip * math.sin(math.radians(angle_degrees / 2))

    dx = l * math.sin(math.radians(c_degr))
    dy = l * math.cos(math.radians(c_degr))

    return [dx, dy]


def get_point_on_circle(center, start_point, angle_degrees):

    if angle_degrees<0:
        angle_degrees=angle_degrees%-360
        angle_degrees+=360


    #right top
    if center[1] >= start_point[1] and center[0] < start_point[0]:
        dx, dy = get_point_on_circle_right_top(center, start_point, angle_degrees)

    #right_bottom
    elif center[1] < start_point[1] and center[0] <= start_point[0]:
        dx, dy = get_point_on_circle_right_bottom(center, start_point, angle_degrees)

    #left top
    elif center[1] > start_point[1] and center[0] >= start_point[0]:
        dx, dy = get_point_on_circle_left_top(center, start_point, angle_degrees)

    #left bottom
    elif center[1] <= start_point[1] and center[0] > start_point[0]:
        dx, dy = get_point_on_circle_left_bottom(center, start_point, angle_degrees)

    else:
        dx, dy = 0, 0

    return dx, dy


def get_point_by_angle(start_point, angle, distance):
    center = [*start_point]
    start_point[1] -= round(distance) #angle 0

    dx, dy = get_point_on_circle(center, [*start_point], angle)
    end_point = [0, 0]
    end_point[0] = start_point[0] + dx
    end_point[1] = start_point[1] + dy

    return end_point

def get_angle_by_point_right_top(center, point):
    dx = point[0] - center[0]
    dy = center[1] - point[1]

    if dx == 0:
        b_degr = 90
    else:
        tanb = dy / dx
        b_degr = math.degrees(math.atan(tanb))

    return b_degr+270

def get_angle_by_point_left_bottom(center, point):
    dx = center[0] - point[0]
    dy = point[1] - center[1]

    if dx == 0:
        b_degr = 90
    else:
        tanb = dy / dx
        b_degr = math.degrees(math.atan(tanb))

    return b_degr+90

def get_angle_by_point_right_bottom(center, point):
    dx = point[0] - center[0]
    dy = point[1] - center[1]

    if dy == 0:
        b_degr = 90
    else:
        tanb = dx / dy
        b_degr = math.degrees(math.atan(tanb))

    return b_degr+180

def get_angle_by_point_left_top(center, point):
    dx = center[0] - point[0]
    dy = center[1] - point[1]

    if dy == 0:
        b_degr = 90
    else:
        tanb = dx / dy
        b_degr = math.degrees(math.atan(tanb))

    return b_degr

def get_angle_by_point(center, point):
    # right top
    if center[1] >= point[1] and center[0] < point[0]:
        return get_angle_by_point_right_top(center, point)

    # right_bottom
    elif center[1] < point[1] and center[0] <= point[0]:
        return get_angle_by_point_right_bottom(center, point)

    # left top
    elif center[1] > point[1] and center[0] >= point[0]:
        return get_angle_by_point_left_top(center, point)

    # left bottom
    elif center[1] <= point[1] and center[0] > point[0]:
        return get_angle_by_point_left_bottom(center, point)

# def rot(an, orig_im, orig_point):
#     import pygame
#     rt_im = pygame.transform.rotate(orig_im, an)
#
#     orig_center = orig_im.get_rect().center
#     dx, dy = get_point_on_circle2(orig_center, orig_point, an)
#
#     rt_center = [*orig_center]
#     rt_center[0] -= round(dx)
#     rt_center[1] -= round(dy)
#
#     rt_rect = pygame.Rect(0, 0, rt_im.get_width(), rt_im.get_height())
#     rt_rect.center = rt_center
#
#     # rt_rect.move_ip(500, 500)
#
#     w.fill([0, 0, 0])
#     w.blit(orig_im, [0, 0])
#     w.blit(rt_im, rt_rect)
#     pygame.display.flip()


# def make_circle(screen, center, start_point, step):
#     import pygame, time, image_modifier
#     pygame.draw.circle(screen, [0, 0, 255], center, 4)
#     pygame.draw.circle(screen, [0, 255, 0], start_point, 4)
#     for i in range(0, -360, -1):
#         print(i)
#         # dx, dy = image_modifier.ImageRotator._get_point_on_circle2(center, start_point, i)
#         dx, dy = get_point_on_circle(center, start_point, i)
#         p = [0, 0]
#         p[0] = start_point[0] + dx
#         p[1] = start_point[1] + dy
#
#         pygame.draw.circle(screen, [255, 0, 0], [round(p[0]), round(p[1])], 2)
#         pygame.display.flip()
#         time.sleep(0.01)
#
#         # start_point=[*p]

# import wrap_base
# math_utils.make_circle(wrap_base.world._window, [600, 600], [630, 550], -5)#right top
# math_utils.make_circle(wrap_base.world._window, [600, 600], [630, 650], 3) #right bottom
# math_utils.make_circle(wrap_base.world._window, [600, 600], [530, 550], 3) #left top
# math_utils.make_circle(wrap_base.world._window, [600, 600], [530, 650], 3) #left bottom
# math_utils.make_circle(wrap_base.world._window, [600, 600], [600, 550], -5)#top
# math_utils.make_circle(wrap_base.world._window, [600, 600], [600, 650], -5)#bottom
# math_utils.make_circle(wrap_base.world._window, [600, 600], [550, 600], -5)#left
# math_utils.make_circle(wrap_base.world._window, [600, 600], [650, 600], -5)#right

def calc_size_proportionally(size1_mod, size1_orig, size2_orig):
    #works if both sizes is 0
    if size1_mod == size1_orig:
        return size2_orig

    scale = size1_mod/size1_orig
    return scale*size2_orig

def get_sizes_proportionally(size1_orig, size2_orig, size1_mod, size2_mod):
    assert size1_mod is not None or size2_mod is not None, "At least one of sizes must be defined"

    #both sized defined
    if size1_mod is not None and size2_mod is not None:
        return [int(size1_mod), int(size2_mod)]

    if size1_mod is not None:
        size2_mod = calc_size_proportionally(size1_mod, size1_orig, size2_orig)
        return [size1_mod, size2_mod]

    if size2_mod is not None:
        size1_mod = calc_size_proportionally(size2_mod, size2_orig, size1_orig)
        return [size1_mod, size2_mod]