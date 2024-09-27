import pygame, model


def control():
    # time.sleep(0.01)
    events = pygame.event.get()

    for i in model.regeneration.spisoc:
        if len(i)== 4:
            i['tower'].control_point(events)
        print(len(i))

    model.apple.control_point(events)
    model.animated_red_portal.control_center(events)
    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)

