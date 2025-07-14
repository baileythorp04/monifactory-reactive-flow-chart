import pygame
from node import Node, Object
import types

def create_node(pos: pygame.Vector2):
    width = 100
    height = 60

    pos.x -= width/2 #create at center
    pos.y -= height/2
    objects.append(Node(pos, width, height))

pygame.init()
screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()

objects = []
dragged_node = Object()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button
            click_xy = pygame.mouse.get_pos()
            click_pos = pygame.Vector2(click_xy)

            if button == 1: #left click
                for obj in objects:
                    if(obj.rect.pygame_rect().collidepoint(click_pos)):
                        dragged_node = obj
                        obj.click(click_pos)
                        break


            elif button == 3: #right click:
                
                create_node(click_pos)
            

        elif event.type == pygame.MOUSEBUTTONUP:
            button = event.button

            if button == 1: #left click
                dragged_node.unclick()
                dragged_node = Object()

    


    for obj in objects:
        obj.update(objects)


    screen.fill((170, 238, 187))    

    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60)