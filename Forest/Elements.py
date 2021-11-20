import random
from typing import ValuesView
import numpy as np

class Unit(object):
    """Элемент на плоскости. Базовый класс."""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        self._position = np.zeros(2,int)
        self._full = False
        self._name = ""
  
    # Свойство X. Координата по горизонтали
    @property 
    def X(self):
        return self._position[0]
    @X.setter
    def X(self, value):
        try:
            self._position[0] = int(value)
        except:
            print("Unit.X – введённое значение не является целым числом")

    # Свойство Y. Координата по вертикали
    @property
    def Y(self):
        return self._position[1]
    @Y.setter
    def Y(self, value):
        self._position[1] = value

    # Свойство Position. Положение объекта на карте
    @property
    def Position(self):
        return self._position
    @Position.setter
    def Position(self, value):
        self._position = value

    # Свойство Full. Показывает, занимает ли объект всю ячейку. Если да, то на эту ячейку больше не может попасть ни один другой элемент
    @property 
    def Full(self):
        return self._full
    @Full.setter
    def Full(self, value):
        self._full = value

    # Свойство Name. Название объекта.
    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, value):
        self._name = value


class Lifeless (Unit):
    """Неживые объекты на поверхности"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        self._jump_over = True

    # Свойство JumpOver. Определяет, можно ли перепыгнуть данный объект.
    @property 
    def JumpOver(self):
        return self._jump_over
    @JumpOver.setter
    def JumpOver(self, value):
        self._jump_over = value


class Food(Unit):
    """Биологические объекты, являющиеся едой"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        self._energy = 0.0
        self._isplant = False
        self._size = 0
        self._fresh = False
        self._timeofendlife = 0
        self._freshtime = 0

    # Свойство Energy. Определяет энергетическую ценность объекта
    @property
    def Energy(self):
        return self._energy
    @Energy.setter
    def Energy(self, value):
        try:
            self._energy = float(value)
        except:
            print("Food.Energy – введённое значение не является числом")

    # Свойство IsPlant. Определяет растительная пища или нет
    @property
    def IsPlant(self):
        return self._isplant
    @IsPlant.setter
    def IsPlant(self, value):
        try:
            self._isplant = bool(value)
        except:
            print("Food.IsPlant – введённое значение не является переменной типа Bool")
        self._freshtime = 0

    @property
    def TimeOfEndLife(self):
        return self._timeofendlife
    @TimeOfEndLife.setter
    def TimeOfEndLife(self,value):
        try:
            self._timeofendlife=int(value)
        except:
            print("Food.TimeofLife не является целым числом")

    @property 
    def FreshTime(self): 
        return self._freshtime
    @FreshTime.setter
    def FreshTime(self,value):
        try:
            self.freshtime=int(value) 
        except:
            print("Food.FreshTime не является целым числом") 
        self._freshtime = 0

    # Свойство TimeOfEndLife. Определяет время с момента прекращения жизнедеятельности
    @property
    def TimeOfEndLife(self):
        return self._timeofendlife
    @TimeOfEndLife.setter
    def TimeOfEndLife(self,value):
        try:
            self._timeofendlife=int(value)
        except:
            print("Food.TimeofLife не является целым числом")

    # Свойство FreshTime. Определяет время, после которого объект испортится
    @property 
    def FreshTime(self): 
        return self._freshtime
    @FreshTime.setter
    def FreshTime(self,value):
        try:
            self.freshtime=int(value) 
        except:
            print("Food.FreshTime не является целым числом") 