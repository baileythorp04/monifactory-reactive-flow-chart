import pygame

def add_xy(xy_1, xy_2):
    return(xy_1[0] + xy_2[0], xy_1[1] + xy_2[1])

def draw_text(font :pygame.font.Font, surface: pygame.Surface, text="empty text", pos = (0,0), color: str | tuple[int,int,int] = "black",  aa = False):
    text_surface = font.render(text, aa, color)
    surface.blit(text_surface, pos)