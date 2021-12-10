import numpy as np

class Field(object):
    """Поле для симуляции"""

    def __init__(self):
        self._ground = np.array([1000,1000])
        self._day_time = True

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

