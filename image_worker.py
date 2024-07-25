import pygame
def to_grayscale(surface):
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height),pygame.SRCALPHA)
    for y in range(height):
        for x in range(width):
            r, g, b, a = surface.get_at((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)  # Преобразование в оттенки серого
            grayscale_surface.set_at((x, y), (gray, 0, 0, a))
    return grayscale_surface

def poly_prosrathnost(surface:pygame.Surface,number):
    s2=surface.convert_alpha()
    s2.set_alpha(number)
    width, height = surface.get_size()
    grayscale_surface = pygame.Surface((width, height),pygame.SRCALPHA)
    grayscale_surface.blit(s2,[0,0])
    return grayscale_surface