import ProgramInterface
import numpy as np
import pygame
import pathlib
import Fonts
import random

AnimalDir = pathlib.Path("sprites", "animals")

class Region(ProgramInterface.Window):
    '''Базовый класс области'''
    def __init__(self, position:np.array, size:np.array):
        super().__init__(position, size)
        self._size = size
        self._max:int = 0
        self._number:float = 0.
        self._a:float = 0.      
        width = size[0]
        height = size[1]
        x = position[0]
        y = position[1]
        self._position = position
        self.Size = size
        self._object_img = pygame.image.load(pathlib.Path(AnimalDir, "Bunny16x16.png")).convert_alpha()
        object_count = self.Number
        self.image.blit(self._object_img, ((width - self._object_img.get_width()) / 2, (height - self._object_img.get_height()) / 2))
        self._isplant = True
        self._biomass = self.Number

    @property
    def IsPlant(self):
        return self._isplant
    @IsPlant.setter
    def IsPlant(self, value):
        self._isplant = bool(value) 

    @property
    def Biomass(self):
        return self._biomass 

    @property
    def Max(self):
        '''Максимальное количество особей, которое может выдержать среда'''
        return self._max
    @Max.setter
    def Max(self, value):
        try:
            if value < 0:
                print('Недопустимое значение Regions.Max')
            else:
                self._max = int(value)
        except:
            print('Недопустимое значение Pegions.Max')

    @property
    def Number(self):
        '''Количество особей на данный момент'''
        return int(self._number)
    @Number.setter
    def Number(self, value):
        try:
            if value < 0:
                print('Недопустимое значение Regions.Number')
                return
            if value == 0:
                self.kill()
                return
            self._number = float(value)
        except:
            print('Недопустимое значение Regions.Number')

    @property
    def A(self):
        '''Удельный прирост'''
        return self._a
    @A.setter
    def A(self, value):
        try:
            self._a = float(value)
        except:
            print('Недопустимое значение Regions.A')

    @property
    def X(self):
        return random.randint(self._position[0], self._position[0] + self.Size[0]) / 16

    @property
    def Y(self):
        return random.randint(self._position[1], self._position[1] + self.Size[1]) / 16

    @property
    def Position(self):
        return np.array([self.X, self.Y])

    def SetMax(self):
        pass        
    
    def Eat(self):
        pass

    def Multiply(self):
        pass

    def Draw(self, size:np.array):
        width = size[0]
        height = size[1]
        self.image.fill((0, 0, 0, 120)) #0x00000078
        self.region_rect = self.image.get_rect()
        self.reion_center = self.region_rect.center
        Label = Fonts.MainFont.render(str(self.Number), True, (255, 255, 255, 255))
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        self.image.blit(self._object_img, ((width - self._object_img.get_width()) / 8, (height - self._object_img.get_height()) / 8))
        self.Border() 




    def update(self):
        self.SetMax()
        self.Eat()
        self.Multiply()
        self.Draw(self._size)

class Ferhulst(Region):
    def __init__(self, position, size):
        super().__init__(position, size)

    def Multiply(self):
        key1 = 1 - (self.Number / self.Max)
        DeltaNumber = key1 * self.A * self.Number
        self.Number += DeltaNumber

class BunnyRegion(Ferhulst):
    def __init__(self, position, size):
        super().__init__(position, size)


class GrassRegion(Ferhulst):
    def __init__(self, position, size):
        super().__init__(position, size)
        self._square = size[0] * size[1] / (16**2)
        self.Max = 440 * self._square
        self._object_img = pygame.image.load(pathlib.Path(AnimalDir, "spider16x16.png")).convert_alpha() 
        self.A = 1.2 * 10**(-9)
        self.Number = 1 
        self.Show = True
        Label = Fonts.MainFont.render(str(self.Number), True, (255, 255, 255, 255))
        width = size[0]
        height = size[1]
        self.image.blit(Label, ((width - Label.get_width()) / 2, (height - Label.get_height()) / 2))
        self.image.blit(self._object_img, ((width - self._object_img.get_width()) / 8, (height - self._object_img.get_height()) / 8))

    def update(self):
        self.Multiply()     
        self.Draw([50, 50])