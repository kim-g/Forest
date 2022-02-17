import Elements
import pygame
import pathlib
import numpy as np

PlantDir = pathlib.Path(pathlib.Path(__file__).parent, "sprites", "plants")

######################################################################################################################
# Класс травы
######################################################################################################################
class Grass(Elements.Plants):
    def __init__(self):
        super().__init__()
        img = pygame.image.load(pathlib.Path(PlantDir, "grass.png")).convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (self.X * 16 + 8, self.Y * 16 + 8)

    def Step(self):
        self.photosyntes(True)

    def update(self):
        self.Step()
        self.rect.center = (self.X * 16 + 8, self.Y * 16 + 8)
