import random
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
        super().__init__()
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
    def Size(self):
        return self._size
    @Size.setter
    def Size(self,value):
        try:
            s = int(value)
            if s >= 0 and s < 4:
                self._size = int(value)
            else:
                print("Food.Size не является допустимым знаением")
        except:
            print("Food.Size не является допустимым знаением")

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


class Animal(Food):
    """Животные. Базовый класс"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        super().__init__()
        self._foodtype = 0 # 0 - травоядное, 1 - хищное , 2 - всеядное
        self._foodsize = 0 
        self._speed = 0
        self._sleeptime = 0 # 0 - ночное, 1 - дневное, 2 - и то и другое
        self._animaltype = 0 # 0 - простейшее, 1 - 

    # Свойство FoodType. Определяет тип пищи, которым объект питается
    @property
    def FoodType(self):
        return self._foodtype
    @FoodType.setter
    def FoodType(self,value):
        try:
            ft = int(value)
            if ft >= 0 and ft < 3:
                self._foodtype = value 
            else:
                print("Animal.FoodType не является допустимым значением")
        except:
            print("Animal.FoodType не является допустимым значением")

    # Свойство FoodSize. Определяет размер пищи, предпочитаемый объектом
    @property
    def FoodSize(self):
        return self._foodsize
    @FoodSize.setter
    def FoodSize(self,value):
        try:
            fs = int(value)
            if fs >= 0 and fs < 4:
                self._foodsize = value
            else:
                print("Animal.FoodSize не является допустимым значением")
        except:
            print("Animal.FoodSize не является допустимым значением")

    # Свойство Speed. Определяет скорость объекта
    @property
    def Speed(self):
        return self._speed
    @Speed.setter
    def Speed(self,value):
        try:
            self._speed = int(value)
        except:
            print("Animal.Speed не является целым числом")

    # Свойство SleepTime. Определяет время, в которое животное спит
    @property
    def SleepTime(self):
        return self._sleeptime
    @SleepTime.setter
    def SleepTime(self,value):
        try:
            st = int(value)
            if st >= 0 and st < 3:
                self._sleeptime = value
            else:
                print("Animal.SleepTime не является допустимым значением")
        except:
            print("Animal.SleepTime не является допустимым значением")

    # Метод Eat. Проверяет может ли животное съесть обект и в зависимости от результата изменяет энергию животного
    def Eat(self, food):
        CanEat = False
      
        # Проверка для травоядных
        if self._foodtype == 0:
            if food.IsPlant:
                if food.Size == self._foodsize:
                    CanEat = True
                else:
                    CanEat = False
            else:
                CanEat = False
        
        # Проверка для хищников
        if self._foodtype == 1:
            if food.IsPlant:
                CanEat = False
            else:
                if food.Size == self._foodsize:
                    CanEat = True
                else:
                    CanEat = False
        
        # Проверка для всеядных
        if self._foodtype == 2:
            if food.Size == self._foodsize:
                CanEat = True
            else:
                CanEat = False

        # Изменение энергии
        if CanEat:
            self.Energy += food.Energy

class Plants(Food):
    """Базовый класс растений"""
    def _init_(self):
        super().__init__()
        self._amofchl = 0.0
        self._toxicity = False
        self._plant_type = 0

    # Количество хлорофила 0 - отсутствует, 1 - мало, 2 - среднее, 3 - много
    @property 
    def AmountOfChlorophill(self):
        return self._amofchl
    @AmountOfChlorophill.setter
    def AmountOfChlorophill(self,value):
        try:
            self.amofchl=int(value) 
        except:
            print("Plants.AmOfChl не является целым числом")
                  
    # Токсичность 0 - нетоксично, 1 - малотоксичный (неприятно), 2 - среднетоксичный (болезнь) 3 - Смертельный 
    @property
    def Toxicity(self):
        return self._toxicity
    @Toxicity.setter
    def Toxicity(self,value):
        try:
            self.toxicity=int(value) 
        except:
            print("Plants.Toxicity не является целым числом") 
    
    # Тип растения. 0 - Водоросль, 1 - Мох, 2 - Папоротник, 3 - Голосеменное, 4 - Цветковое
    @property 
    def PlantType(self):
        return self._plant_type
    @PlantType.setter
    def PlantType(self,value):
        try:
            self._plant_type=int(value) 
        except:
            print("Plants.PlantType не является целым числом")
            print("Food.FreshTime не является целым числом") 

class Plants(Unit):
    def __init__(self):
        self._amofchl=0.0
        self._toxicity=False
        self._flowerspresence=False
    @property 
    def AmOfChl(self):
        return self._amofchl
    @AmOfChl.setter
    def AmOfChl(self,value):
        try:
            self.amofchl=int(value) 
        except:
            print("Plants.AmOfChl не является целым числом") 
    @property 
    def Toxicity(self):
        return self._toxicity
    @Toxicity.setter
    def Toxicity(self,value):
        try:
            self.toxicity=int(value) 
        except:
            print("Plants.Toxicity не является целым числом") 

    @property 
    def FlowersPresence(self):
        return self._flowerspresence
    @FlowersPresence.setter
    def FlowersPresence(self,value):
        try:
            self.flowerspresence=int(value) 
        except:
            print("Plants.FlowersPresence не является целым числом")