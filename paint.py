import pygame

import kakoito_resizer
import math_utils

pygame.init()
screen = pygame.display.set_mode([900, 800])
font = pygame.font.SysFont('arial', 50)

import model

def risovanie():
    model.clock.tick()
    fps=model.clock.get_fps()
    pygame.display.flip()
    for p in model.tutorial_level.plitki:
        p.okraska(screen)




    #надписи

    for g in model.bazar:
        g.paint(model.wallet.money>=g.numprice)
    model.wallet.grafiti(800,0)




    images=[model.tutorial_level.animated_red_portal,model.tutorial_level.animated_blue_portal]

    # for i in model.plitki:
    #     if i.building == 'tower':
    #         images.append(i.tower)

    # for i in model.enemys:
    #     images.append(i)

    images+=model.enemys


    # for p in  range(len(model.enemys)-1,-1,-1):
    #     if model.enemys:
    #         model.enemys[p].paint()


    # рисование башни на квадрате с мышкой
    j = math_utils.poisk_kletki(pygame.mouse.get_pos(),model.tutorial_level.plitki)
    if j!=None and model.apple!=None:
        rect=j.get_rect()
        if j.type == 'grass' and j.building==None:
            model.apple.colored_drawer(prozrathnost=200)
        else:
            model.apple.colored_drawer(True)
    model.tutorial_level.paint(model.perecluthatel,images)



    if model.perecluthatel:
        shoti=0
        for u in model.route:
            pygame.draw.circle(screen,[0,0,0],u,10)
            pos=font.render(str(shoti),True,[255,0,0])
            screen.blit(pos,u)
            shoti+=1

        show_fps=font.render(str(int(fps)),True,[255,0,0])
        screen.blit(show_fps,[10,20])

    for m in model.bullets:
        m.okraska()


