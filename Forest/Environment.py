import numpy as np

class Field(object):
    """Поле для симуляции"""
    def __init__(self):
        self._ground = np.array([1000,1000])
        self._day_time = True
        self.alive = []
        self.elements = []

    @property
    def Ground(self):
        return self._ground
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

    @property
    def Elements(self):
        return self.elements
    @Elements.setter
    def Elements(self, value):
        try:
            self.elements.append(value)
        except:
            print('невозможно добавить значение в список elements')
    @property
    def Alive(self):
        return self.alive
    @Alive.setter
    def Alive(self, value):
        try:
            self.alive.append(value)
        except:
            print('невозможно добавить значение в список alive')