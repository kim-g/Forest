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
        self._parent = None

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
    
    # Свойство Parent. Определяет родителей объекта
    @property 
    def Parent(self):
        return self._parent
    @Parent.setter
    def Parent(self, value):
        self._parent = value

    # Абстрактный метод совершения действия
    def Step(self):
        pass


class Animal(Food):
    """Животные. Базовый класс"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        super().__init__()
        self._foodtype = 0 # 0 - травоядное, 1 - хищное , 2 - всеядное
        self._foodsize = 0 
        self._speed = 0
        self._sleeptime = 0 # 0 - ночное, 1 - дневное, 2 - и то и другое
        self._animaltype = 0 # 0 - простейшее, 1 - плоские черви, 2 - круглые черви, 3 - кольчатые черви, 4 - кишечнополостные, 5 - членистоногие, 6 - моллюски, 7 - иглокожие, 8 - хордовые 
        self._rotteneattype = 0 # 0 - не ест гниль, 1 - ест только гниль, 2 - безразлично
        self._aim = np.zeros(2, int)

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

    # Свойство AnimalType. Определяет тип животного
    @property
    def AnimalType(self):
        return self._animaltype
    @AnimalType.setter
    def AnimalType(self,value):
        try:
            at = int(value)
            if st >= 0 and st < 9:
                self._animaltype = value
            else:
                print("Animal.AnimalType не является допустимым значением")
        except:
            print("Animal.AnimalType не является допустимым значением")

    # Свойство RottenEatType. Определяет какие предпочтения в свежести у объекта
    @property
    def RottenEatType(self):
        return self._rotteneattype
    @RottenEatType.setter
    def RottenEatType(self,value):
        try:
            ret = int(value)
            if st >= 0 and st < 3:
                self._sleeptime = value
            else:
                print("Animal.RottenEatType не является допустимым значением")
        except:
            print("Animal.RottenEatType не является допустимым значением")

    # Свойство Aim. Определяет координаты, на которое животное хочет переместиться животное
    @property
    def Aim(self):
        return self._aim
    @Aim.setter
    def Aim(self, value):
        self._aim = value

    # Метод Eat. Проверяет может ли животное съесть обект и в зависимости от результата изменяет энергию животного
    def Eat(self, food):
        CanEat = False
      
        # Проверка для травоядных
        if self._foodtype == 0:
            if food.IsPlant:
                if food.Size == self._foodsize:
                    CanEat = True
        
        # Проверка для хищников
        if self._foodtype == 1:
            if food.IsPlant:
                CanEat = False
            else:
                if food.Size == self._foodsize:
                    CanEat = True
        
        # Проверка для всеядных
        if self._foodtype == 2:
            if food.Size == self._foodsize:
                CanEat = True

        # Изменение энергии
        if CanEat:
            self.Energy += food.Energy

    # Метод Move. Передвижение
    def Move(self):
        StartPos = self.Position
        for i in range(0, self.Speed):
            V = np.array([self.Aim[0] - self.Position[0], self.Aim[1] - self.Position[1]])
            x1 = abs(V[0])
            y1 = abs(V[1])
            V1 = np.array([0 if V[0] == 0 else int(V[0] / x1), 0 if V[1] == 0 else int(V[1] / y1)])
            M = max(x1, y1)
            m = min(x1, y1)
            if M > 1.5 * m:
                if x1 > y1 :
                    self.Position[0] += V1[0]
                else:
                    self.Position[1] += V1[1]
            else:
                self.Position[0] += V1[0]
                self.Position[1] += V1[1]

        #Parent.Ground[StartPos[0], StartPos[1]].remove(self)
        #Parent.Ground[Position[0], Position[1]].append(self)

    # Итерация действия у животного.
    def Step(self):
        super().Step()

        if self.Aim[0] == self.Position[0] and self.Aim[1] == self.Position[1]:
            self.Aim = np.array([random.randint(0, self.Parent.Width), random.randint(0, self.Parent.Height)])
            print("Я сменил цель на ", self.Aim)
        self.Move()
        print ("Ход на ", self.Position)

class Plants(Food):
    """Базовый класс растений"""
    def _init_(self):
        super().__init__()
        self._amountofchlorophill = 0.0
        self._toxicity = False
        self._plant_type = 0

    # Количество хлорофила 0 - отсутствует, 1 - мало, 2 - среднее, 3 - много
    @property 
    def AmountOfChlorophill(self):
        return self._amountofchllorophill
    @AmountOfChlorophill.setter
    def AmountOfChlorophill(self,value):
        try:
            self._amountofchllorophill=int(value) 
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

    def photosyntes(self,light):
        #if not bool(light):
        #    return
        K=50
        E = K*self.AmountOfChlorophill
        if self._size==0:
            self.Energy += E* 0.01
            return
        if self._size==1:
            self.Energy += E*1
            return
        if self._size==2:
            self.Energy += E*10
            return
        if self._size==3:
            self.Energy += E*20
            return
        print("Error eating")