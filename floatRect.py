import pygame

class FloatRect():
    def __init__(self,pos,size):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
    
    def move(self, vector):
        return FloatRect((self.x+vector[0], self.y+vector[1]), (self.width, self.height))

    def move_ip(self, vector):
        self.x += vector[0]
        self.y += vector[1]
    
    def move_to(self, pos):
        self.x = pos[0]
        self.y = pos[1]
    
    def center(self):
        return pygame.Vector2(self.x+self.height/2, self.y+self.height/2)
    
    def top_left(self):
        return pygame.Vector2(self.x, self.y)

    def pygame_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def x_right(self):
        return self.x + self.width
    
    def y_bottom(self):
        return self.y + self.height
