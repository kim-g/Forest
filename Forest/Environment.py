from typing import List
import numpy as np

class Field(object):
    """Поле для симуляции"""
    def __init__(self):
        self.Height = 1000
        self.Width = 1000
        self._ground = np.zeros([self.Width,self.Height])
        #for i in range (0, self.Width):
        #    for j in range (0, self.Height):
        #        self._ground[i,j] = list()
        self._day_time = True
        self._elements = list() 
        self._alive = list() 

    #Elements
    #Alive

    @property 
    def Alive(self):
        return self._alive
    @Alive.setter
    def alive(self,value):
        try:
            self._alive=value
        except:
            pass
            
    @property 
    def Elements(self):
        return self._elements
    @Elements.setter
    def elements(self,value): 
        try:
            self._elements=value
        except:
            pass


    @property
    def Ground(self):
        return self._ground
    @Ground.setter
    def Ground (self, value):
        pass

    def Watch(self, pos, r):
        pass

    @property 
    def DayTime(self): #изменяет значение дня
        return self._day_time
    @DayTime.setter
    def DayTime(self, value):
        try:
            self._day_time = bool(value)
        except:
            print("Field.Daytime не является булеевым значением")

    @property
    def Elements(self):
        return self._elements
    @Elements.setter
    def Elements(self, value):
        try:
            self._elements = value
        except:
            print('невозможно добавить значение в список elements')
    @property
    def Alive(self):
        return self._alive
    @Alive.setter
    def Alive(self, value):
        try:
            self._alive = value
        except:
            print('невозможно добавить значение в список alive')