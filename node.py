import pygame
class Node():
    def __init__(self, pos, width, height):
        #define init variables
        self.rect = pygame.Rect(pos, (width, height))
        #text
        #image / type (dust, fluid)
        #color
        
    def draw(self, surface):

        pygame.draw.rect(surface, "black", self.rect, 2)
        #draw box outline
        #draw text
        #draw image
        pass

    def update(self):
        self.repel_from_edge()
        self.rect.move_ip(1, 0)

    def repel_from_other(self, other):
        #if close to another node, move away from it
        pass

    def repel_from_edge(self):
        pass

    