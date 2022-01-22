import Elements
import pygame
import numpy as np
import pathlib
import math
import random

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
        self._aim_sprite = Elements.Aim()

    def Move(self, force):
        super().Move(force)
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))

    def Step(self):#надо передать цель для движения
        super().Step()
        self._aim_sprite.Position = self.Aim

    def update(self):
        self.Step()

    def SetAim(self):
        angle = random.randint(0,360) / 180 * math.pi
        self.Aim[0] += math.cos(angle) * 3
        self.Aim[1] += math.sin(angle) * 3
        if self.Aim[0] < 0:
            self.Aim[0] = 0;
        if self.Aim[1] < 0:
            self.Aim[1] = 0;
        if self.Aim[0] >= self.Parent.Width:
            self.Aim[0] = self.Parent.Width - 1;
        if self.Aim[1] >= self.Parent.Height:
            self.Aim[1] = self.Parent.Height - 1;

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

    
    def SetAim(self):
        Aims= list(filter(lambda x: self.Path(x)<10,self.Parent.Alive))
        AimsCount=len(Aims)
        if AimsCount ==0:
            super().SetAim()
            return
        if AimsCount ==1:
            Aim = Aims[0].Position
            return
        Aim=Aims[random.randint(0,AimsCount)].Position
         

class Chameleon(Elements.Animal):
    def __init__(self):

        super().__init__()
        chameleon_img = pygame.image.load(pathlib.Path(AnimalDir, "chameleon16x16.png")).convert_alpha()
        self.image = chameleon_img
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



    