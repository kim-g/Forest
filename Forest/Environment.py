import numpy as np

class Field(object):
    """Поле для симуляции"""
    def __init__(self):
        self._ground = np.array([1000,1000])
        self._day_time = True

    @property
    def Ground(self):
        return self._ground
    @Ground.setter
    def Ground (self, value):
        pass

    def Watch(self, pos, r):
        pass

    @property 
    def DayTime(self):
        pass
    @DayTime.setter
    def DayTime(self, value):
        pass

    @property
    def Elements(self):
        pass
    @Elements.setter
    def Elements(self, value):
        pass

    @property
    def Alive(self):
        pass
    @Alive.setter
    def Alive(self, value):
        pass