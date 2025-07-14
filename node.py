import pygame
import math
from floatRect import FloatRect

class Object():
    def draw(self):
        print("draw not overridden")

    def update(self):
        print("update not overridden")


#eventually split Node into Recipe and Item child classes
class Node(Object):

    repel_distance = 150
    repel_speed = 3

    def __init__(self, pos, width, height):
        #define init variables
        self.rect = FloatRect(pos, (width, height))
        #text
        #image / type (dust, fluid)
        #color
        
    def draw(self, surface):

        pygame.draw.rect(surface, "black", self.rect.pygame_rect(), 2)
        #draw box outline
        #draw text
        #draw image


    def update(self, objects):
        for obj in objects:
            if obj is not self:
                #if obj is a node
                self.repel_from_other(obj)

    def repel_from_other(self, other):
        self_x, self_y = self.rect.center()
        other_x, other_y = other.rect.center()
        line = pygame.Vector2(self_x - other_x, self_y - other_y)

        if line.length() < self.repel_distance * 0.9: #stop repelling if its 90% of the way there so it doesnt take forever to stop
            repel_ratio = (self.repel_distance / line.length()) - 1 #repel faster when closer
            self.move(line.normalize() * repel_ratio * self.repel_speed) 


    def move(self, disp):
        self.rect.move_ip(disp)
        #move while accounting for edges
