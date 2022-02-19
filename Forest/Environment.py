from typing import List
import numpy as np

class Field(object):
    """Поле для симуляции"""
    def __init__(self, monitor_info):
        self.Height = int(monitor_info.current_h / 16)
        self.Width = int(monitor_info.current_w / 16)
        self._ground = np.zeros([self.Width,self.Height])
        #for i in range (0, self.Width):
        #    for j in range (0, self.Height):
        #        self._ground[i,j] = list()
        self._day_time = True
        self._elements = list() #список всех элементов
        self._alive = list() #список живых объектов

    
    #Свойство Alive. Определяет список всех живых объектов

    @property
    def Alive(self):
        return self._alive
    @Alive.setter
    def Alive(self, value):
        try:
            self._alive = value
        except:
            print('невозможно добавить значение в список alive')

    #Свойство Elements. Определяет список абсолютно  всех объектов      

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
    def Ground(self):
        return self._ground
    @Ground.setter
    def Ground (self, value):
        pass

    def Watch(self, pos, r):
        pass

    # свойство изменяет значение дня

    @property 
    def DayTime(self):
        return self._day_time
    @DayTime.setter
    def DayTime(self, value):
        try:
            self._day_time = bool(value)
        except:
            print("Field.Daytime не является булеевым значением")

    def Delete(self, obj):
        self.Elements.remove(obj)
        self.Alive.remove(obj)
