import pygame

def to_grayscale_with_color(surface, color=(255, 0, 0)):
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    for y in range(height):
        for x in range(width):
            r, g, b, a = surface.get_at((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)  # Преобразование в оттенки серого

            # Применяем оттенок серого к заданному цвету
            r_colored = int(gray * (color[0] / 255))
            g_colored = int(gray * (color[1] / 255))
            b_colored = int(gray * (color[2] / 255))

            grayscale_surface.set_at((x, y), (r_colored, g_colored, b_colored, a))

    return grayscale_surface


def poly_prosrathnost(surface:pygame.Surface,number):
    s2=surface.convert_alpha()
    s2.set_alpha(number)
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height),pygame.SRCALPHA)
    grayscale_surface.blit(s2,[0,0])
    return grayscale_surface