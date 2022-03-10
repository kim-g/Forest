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
#        Aims = ["Fox", "Turtle", "Beast"]
#        Elements.Animal().Aim_1_Atack(Aims)

        angle = random.randint(0,360) / 180 * math.pi
        self.Aim[0] += math.cos(angle) * 3
        self.Aim[1] += math.sin(angle) * 3
        if self.Aim[0] < 0:
            self.Aim[0] = 0
        if self.Aim[1] < 0:
            self.Aim[1] = 0
        if self.Aim[0] >= self.EcoSystem.Width:
            self.Aim[0] = self.EcoSystem.Width - 1
        if self.Aim[1] >= self.EcoSystem.Height:
            self.Aim[1] = self.EcoSystem.Height - 1

######################################################################################################################
# Класс черпахи
# Всё время ходит.
# Целью выбирается ближайшая трава
######################################################################################################################

class Turtle(Elements.Animal):
    def __init__(self):

        super().__init__()
        turtle_img = pygame.image.load(pathlib.Path(AnimalDir, "turtle16x16.png")).convert_alpha()
        self.image = turtle_img
        self.Out_Image = turtle_img
        self.Hole_Image = pygame.image.load(pathlib.Path(AnimalDir, "turtle_hole16x16.png")).convert_alpha()
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
        if not self.HungryFlag:
            self.Aim = self.Position
            self.image = self.Hole_Image
        else:
            self.image = self.Out_Image
            Aims = list(filter(lambda x: self.Path(x)<10 and x.__class__.__name__ == "Grass", self.EcoSystem.Alive))
            AimsCount=len(Aims)
            if AimsCount ==0:
                super().SetAim()
                return
            if AimsCount == 1:
                self.Aim = Aims[0].Position
                self.AimObject = Aims[0]
                return
            if AimsCount < 4:
                self.AimObject = Aims[random.randint(0,AimsCount-1)]
                self.Aim=self.AimObject.Position
                return
            Aims.sort(key= lambda x: self.Path(x))
            self.AimObject = Aims[random.randint(0,3)]
            self.Aim=self.AimObject.Position

    def OnAim(self, Aim):
        self.Eat(Aim)

######################################################################################################################
# Класс кролика
# Всё время ходит
# Целью выбирается ближайшая трава. Если сыт, старается убежать от лисов
######################################################################################################################
class Bunny(Elements.Animal):
    def __init__(self):
        super().__init__()
        bunny_img = pygame.image.load(pathlib.Path(AnimalDir, "Bunny16x16")).convert_alpha()
        self.image = bunny_img
        self.Out_Image = bunny_img
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
        if not self.HungryFlag:
            Dangers = list(filter(lambda x: self.Path(x)<10 and x.__class__.__name__ == "Fox", self.EcoSystem.Alive))
            while Dangers != 0:
                self.Aim = np.array([self.X + 1, self.Y + 1])
            self.Aim = self.Position
        else:
            self.image = self.Out_Image
            Aims = list(filter(lambda x: self.Path(x)<10 and x.__class__.__name__ == "Grass", self.EcoSystem.Alive))
            AimsCount=len(Aims)
            if AimsCount ==0:
                super().SetAim()
                return
            if AimsCount == 1:
                self.Aim = Aims[0].Position
                self.AimObject = Aims[0]
                return
            if AimsCount < 4:
                self.AimObject = Aims[random.randint(0,AimsCount-1)]
                self.Aim=self.AimObject.Position
                return
            Aims.sort(key= lambda x: self.Path(x))
            self.AimObject = Aims[random.randint(0,3)]
            self.Aim=self.AimObject.Position

######################################################################################################################
# Класс волка
# Всё время ходит.
# Целью выбирается ближайшие кролики
# Ауф
######################################################################################################################
class Wolf(Elements.Animal):
    def __init__(self):

        super().__init__()
        wolf_img = pygame.image.load(pathlib.Path(AnimalDir, "Wolf16x16.png")).convert_alpha()
        self.image = wolf_img
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))
        self._aim_sprite = Elements.Aim()
        self.wolf_pokushal_img = pygame.image.load(pathlib.Path(AnimalDir, "WolfChill16x16.png")).convert_alpha()

    def Move(self, force):
        super().Move(force)
        self.rect.center = (int(self.X * 16 + 8), int(self.Y * 16 + 8))

    def Step(self):
        super().Step()
        self._aim_sprite.Position = self.Aim

    def update(self):
        self.Step()

    def SetAim(self, food):
        '''Установка цели волка'''
        if not self.HungryFlag:  
            self.image = self.wolf_pokushal_img
            self.Aim = self.Position
        else:
            Aims = list(filter(lambda x: self.Path(x)<10 and x.__class__.__name__ == "Bunny", self.EcoSystem.Alive))
            AimsCount=len(Aims)
            if AimsCount ==0:
                super().SetAim()
                return
            if AimsCount == 1:
                self.Aim = Aims[0].Position
                self.AimObject = Aims[0]
                return
            if AimsCount < 4:
                self.AimObject = Aims[random.randint(0,AimsCount-1)]
                self.Aim=self.AimObject.Position
                return
            Aims.sort(key= lambda x: self.Path(x))
            self.AimObject = Aims[random.randint(0,3)]
            self.Aim=self.AimObject.Position

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