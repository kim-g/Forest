import Elements
import pygame
import os
import numpy as np

PlantDir = os.path.join(os.path.join(os.path.dirname(__file__), "sprites"), "plants")

######################################################################################################################
# Класс травы
######################################################################################################################
class Grass(Elements.Plants):
    def __init__(self):
        super()._init_()
        img = pygame.image.load(os.path.join(PlantDir, "grass.png")).convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (self.X * 16 + 8, self.Y * 16 + 8)

    def Step(self):
        self.photosyntes(True)

    def update(self):
        self.Step()
        self.rect.center = (self.X * 16 + 8, self.Y * 16 + 8)
