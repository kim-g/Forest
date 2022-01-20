import Elements
import pygame
import numpy as np
import pathlib

AnimalDir = pathlib.Path("sprites", "animals")

######################################################################################################################
# Класс абстрактного зверя
# Всё время ходит.
# Цель выбирается случайно
######################################################################################################################
class Beast(Elements.Animal):
    def __init__(self):

        super().__init__()
        beast_img = pygame.image.load(pathlib.Path(AnimalDir, "beast.png")).convert_alpha()
        self.image = beast_img
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))
        self._aim_sprite = Elements.Aim()

    def Move(self, force):
        super().Move(force)
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))

    def Step(self):
        super().Step()
        self._aim_sprite.Position = self.Aim

    def update(self):
        self.Step()



######################################################################################################################
# Класс полярного песца
# Всё время ходит.
# Цель выбирается случайно
######################################################################################################################
class Fox(Elements.Animal):
    def __init__(self):

        super().__init__()
        Fox_img = pygame.image.load(pathlib.Path(AnimalDir, "fox16x16.png")).convert_alpha()
        self.image = Fox_img
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))
        self._line_of_sight_ = Elements.Animal_Aim()

    def Move(self, force):
        super().Move(force)
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))
        self._line_of_sight_.get_distance(5, self.rect.x, self.rect.y)

    def Step(self):#надо передать цель для движения
        pass

    def update(self):
        self.Step()



######################################################################################################################
# Класс черпахи
# Всё время ходит.
# Цель выбирается случайно
######################################################################################################################
class Turtle(Elements.Animal):
    def __init__(self):

        super().__init__()
        turtle_img = pygame.image.load(pathlib.Path(AnimalDir, "turtle16x16.png")).convert_alpha()
        self.image = turtle_img
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))
        self._aim_sprite = Elements.Aim()

    def Move(self, force):
        super().Move(force)
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))

    def Step(self):
        super().Step()
        self._aim_sprite.Position = self.Aim

    def update(self):
        self.Step()