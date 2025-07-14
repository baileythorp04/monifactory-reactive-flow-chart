import pygame
from node import Node, Object
import constants

def create_node(pos: pygame.Vector2):
    width = 100
    height = 60

    pos.x -= width/2 #create at center
    pos.y -= height/2
    nodes.append(Node(pos, width, height))

pygame.init()
screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
clock = pygame.time.Clock()

nodes: list[Node] = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button
            click_xy = pygame.mouse.get_pos()
            click_pos = pygame.Vector2(click_xy)

            if button == 2: #middle click
                create_node(click_pos)
        

        for node in nodes:
            node.handle_event(event)

    


    for node in nodes:
        node.update(nodes)


    screen.fill((170, 238, 187))    

    for node in nodes:
        node.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60)