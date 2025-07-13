import pygame
from node import Node






def create_node(pos):
    objects.append(Node(pos, 50, 20))

pygame.init()
screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()
objects = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            create_node(click_pos)
            pass
    


    for obj in objects:
        obj.update()


    screen.fill((170, 238, 187))    

    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60)