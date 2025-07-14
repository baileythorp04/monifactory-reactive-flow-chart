import pygame
import math
import random
from floatRect import FloatRect
from helpers import *

class Object():
    def draw(self):
        print("draw not overridden")

    def update(self):
        print("update not overridden")
    
    def click(self):
        print("click not overridden")
    
    def unclick(self):
        print("unclick not overridden")


#eventually split Node into Recipe and Item child classes
class Node(Object):

    repel_range = 150
    repel_speed = 3
    being_dragged = False
    dragged_offset = (0,0)

    def __init__(self, pos, width, height):
        pos[0] += random.random() - 0.5
        pos[1] += random.random() - 0.5
        self.rect = FloatRect(pos, (width, height))

        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        self.color = (r,g,b)
        #text
        #image / type (dust, fluid)
        #color
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect.pygame_rect(), 2)
        #draw text
        #draw image


    def update(self, objects):

        if self.being_dragged:
            self.rect.move_to(pygame.mouse.get_pos() + (self.dragged_offset*-1))

        else:
            for obj in objects:
                if obj is not self:
                    #if obj is a node
                    if not obj.being_dragged:
                        self.repel_from_other(obj)
    

    def click(self, click_pos: pygame.Vector2):
        self.being_dragged = True
        self.dragged_offset = click_pos - self.rect.top_left()
    
    def unclick(self):
        self.being_dragged = False


    def repel_from_other(self, other):
        self_x, self_y = self.rect.center()
        other_x, other_y = other.rect.center()
        line = pygame.Vector2(self_x - other_x, self_y - other_y)

        if line.length() < self.repel_range * 0.9: #stop repelling if its 90% of the way there so it doesnt take forever to stop
            repel_ratio = (self.repel_range / line.length()) - 1 #repel faster when closer.
            repel_displacement = line.normalize() * repel_ratio * self.repel_speed
            repel_displacement.clamp_magnitude_ip(30)
            self.move(repel_displacement) 


    def move(self, disp):
        self.rect.move_ip(disp)
        #move while accounting for edges
