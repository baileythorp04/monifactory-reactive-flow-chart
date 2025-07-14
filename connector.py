import pygame
from node import Object

class Connector(Object):
    def __init__(self, n1, n2):
        self.node_1 = n1
        self.node_2 = n2