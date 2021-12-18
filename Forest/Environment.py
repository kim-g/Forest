from typing import List
import numpy as np

class Field(object):
    """Поле для симуляции"""

    def __init__(self):
        self._ground = np.array([1000,1000])
        self._day_time = True
        self._elements=list 
        self._alive=list 

    #Elements
    #Alive

    @property 
    def Alive(self):
        return self._alive
    @Alive.setter
    def alive(self,value):
        try:
            self._alive=int(value)
            
    @property 
    def Elements(self):
        return self._elements
    @Elements.setter
    def elements(self,value) 
    try:
        self._elements=int(value) 


    @property
    def Ground(self):
        pass

    @Ground.setter
    def Ground (self, value):
        pass

    def Watch(self, pos, r):
        pass

    @property 
    def DayTime(self):#изменяет значение дня
        return self._day_time

    @DayTime.setter
    def DayTime(self, value):
        try:
            self._day_time = bool(value)
        except:
            print("Field.Daytime не является булеевым значением")

