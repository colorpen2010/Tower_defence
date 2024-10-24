import pygame, model


def control():
    # time.sleep(0.01)
    events = pygame.event.get()

    model.apple.control_point(events)
    for r in model.spisoc:
        if r.tower!= None:
            r.tower.control_point(events)

    model.animated_blue_portal.control_center(events)
    model.animated_red_portal.control_center(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit()
        if o.type == pygame.KEYDOWN and o.key == pygame.K_TAB:
            model.perecluthatel = not model.perecluthatel
        if o.type == pygame.MOUSEBUTTONDOWN and o.button == pygame.BUTTON_LEFT:
            model.ystanowka_bashni(o.pos)
