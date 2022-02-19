import random
import numpy as np
import pygame
import pathlib
import math
import Environment

InterfaceDir = pathlib.Path(pathlib.Path(__file__).resolve().parent, "sprites", "interface")

class Unit(pygame.sprite.Sprite):
    """Элемент на плоскости. Базовый класс."""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        """Инициализация объекта"""
        self._position = np.zeros(2,float)
        self._full:bool = False
        self._name:str = ""
        pygame.sprite.Sprite.__init__(self)
        self.image:pygame.Surface = pygame.Surface((16, 16))
        self.Y
  
    # Свойство X. Координата по горизонтали
    @property 
    def X(self):
        """Координата объекта на оси абцисс"""
        return self._position[0]
    @X.setter
    def X(self, value:float):
        try:
            value = float(value)
            if not np.isnan(value):
                self._position[0] = value
        except:
            print("Unit.X – введённое значение не является целым числом")

    # Свойство Y. Координата по вертикали
    @property
    def Y(self):
        """Свойство Y. Координата по вертикали"""
        return self._position[1]
    @Y.setter
    def Y(self, value:float):
        try:
            if not np.isnan(value):
                self._position[1] = value
        except:
            print("Unit.Y – введённое значение не является целым числом")

    # Свойство Position. Положение объекта на карте
    @property
    def Position(self):
        return self._position
    @Position.setter
    def Position(self, value):
        self.X = value[0]
        self.Y = value[1]

    # Свойство Full. Показывает, занимает ли объект всю ячейку. Если да, то на эту ячейку больше не может попасть ни один другой элемент
    @property 
    def Full(self):
        """Определяет, занимает ли объект всю ячейку"""
        return self._full
    @Full.setter
    def Full(self, value):
        self._full = value

    # Свойство Name. Название объекта.
    @property
    def Name(self):
        """Название объекта"""
        return self._name
    @Name.setter
    def Name(self, value):
        self._name = value


class Lifeless (Unit):
    """Неживые объекты на поверхности"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        super().__init__()
        self._jump_over = True

    # Свойство JumpOver. Определяет, можно ли перепыгнуть данный объект.
    @property 
    def JumpOver(self):
        """Определяет, можно ли перепрыгнуть через объект"""
        return self._jump_over
    @JumpOver.setter
    def JumpOver(self, value):
        self._jump_over = value


class Food(Unit):
    """Биологические объекты, являющиеся едой"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        super().__init__()
        self._energy:float = 0.
        self._isplant:bool = False
        self._size:int = 0
        self._fresh:bool = False
        self._timeofendlife:int = 0
        self._freshtime:int = 0
        self._parent = None
        self._biomass:float = 0.
        self._top_threshold:float = 0.
        self._energy_coeff:float = 4.
        self._transcoeff:float = 1.
        self._lower_treshold:float = 0.

    # Свойство Energy. Определяет энергетическую ценность объекта
    @property
    def Energy(self):
        """Определяет энергетическую ценность объекта"""
        return self._energy
    @Energy.setter
    def Energy(self, value:float):
        """Определяет энергетическую ценность объекта"""
        try:
            if value<self.Lower_Treshold:
                DeltaE = self.Lower_Trashhold - value
                DeltaM = DeltaE/self._energy_coeff - self._transcoeff
                self.Biomass -= DeltaM
                self._energy=self.Lower_Trashhold
                return


            if value > self.TopTreshold:
                deltae = (self._energy + value) - self.TopTreshold
                biomtransform = self.EnergyCoeff + self.TransCoeff
                deltam = deltae / biomtransform
                self._energy = self.TopTreshold
                self.Biomass += deltam
                return
            self._energy = float(value)
        except:
            print("Food.Energy – введённое значение не является числом") 

    # Свойство IsPlant. Определяет растительная пища или нет
    @property
    def IsPlant(self):
        ''' Определяет растительная пища или нет'''
        return self._isplant
    @IsPlant.setter
    def IsPlant(self, value:bool):
        try:
            self._isplant = bool(value)
        except:
            print("Food.IsPlant – введённое значение не является переменной типа Bool")
        self._freshtime = 0

    @property
    def Size(self):
        '''Определяет размер объекта'''
        return self._size
    @Size.setter
    def Size(self,value:int):
        try:
            s = int(value)
            if s >= 0 and s < 4:
                self._size = int(value)
            else:
                print("Food.Size не является допустимым знаением")
        except:
            print("Food.Size не является допустимым знаением")


    # Свойство TimeOfEndLife. Определяет время с момента прекращения жизнедеятельности
    @property
    def TimeOfEndLife(self):
        '''Определяет время с момента прекращения жизнедеятельности'''
        return self._timeofendlife
    @TimeOfEndLife.setter
    def TimeOfEndLife(self,value:int):
        try:
            self._timeofendlife=int(value)
        except:
            print("Food.TimeofLife не является целым числом")

    # Свойство FreshTime. Определяет время, после которого объект испортится
    @property 
    def FreshTime(self):
        '''Определяет время, после которого объект испортится'''
        return self._freshtime
    @FreshTime.setter
    def FreshTime(self, value:int):
        try:
            self.freshtime=int(value) 
        except:
            print("Food.FreshTime не является целым числом") 
    
    # Свойство Parent. Определяет родителей объекта
    @property 
    def Parent(self):
        '''Определяет родителей объекта'''
        return self._parent
    @Parent.setter
    def Parent(self, value):
        self._parent = value


    @property
    def TransCoeff(self):
        '''Определяет кол-во переработанной энергии в биомассу и обратно'''
        return self._transcoeff
    @TransCoeff.setter
    def TransCoeff(self, value:float):
        try:
            self._transcoeff = float(value)
        except:
            pass

    # Абстрактный метод совершения действия
    def Step(self):
        pass

    # Свойство Biomass. Определяет биомассу объекта
    @property
    def Biomass(self):
        '''Определяет биомассу объекта'''
        return self._biomass
    @Biomass.setter
    def Biomass(self, value:float):
        try:
            self._biomass = float(value)
        except:
            print("Недопустимое значение перменной в Food.Biomass")

    # Свойство TopTreshold. Определяет верхний порог энергии объекта
    @property
    def TopTreshold(self):
        '''Определяет верхний порог энергии объекта'''
        return self._top_treshold
    @TopTreshold.setter
    def TopTreshold(self, value:float):
        try:
            self._top_treshold = float(value)
        except:
            print("Недопустимое значение перменной в Food.TopTreshold")

    # Свойство Lower_Treshold. Определяет нижний порог энергии
    @property
    def Lower_Treshold(self):
        '''Определяет нижний порог энергии'''
        return self._lower_treshold
    @Lower_Treshold.setter
    def Lower_Treshold(self, value:float):
        try:
            self._lower_treshold = float(value)
        except:
            print('Food.Lower_Treshold не Float')

    # Свойство EnergyCoeff. Определяет коэффициент энергии, нужный для синтеза материи
    @property
    def EnergyCoeff(self):
        '''Определяет коэффициент энергии, нужный для синтеза материи'''
        return self._energy_coeff
    @EnergyCoeff.setter
    def EnergyCoeff(self, value:float):
        try:
            self._energy_coeff = float(value)
        except:
            print("Недопустимое значение перменной")

    # Свойство Energy. Определяет энергетическую ценность объекта
    @property
    def Energy(self):
        '''Определяет энергетическую ценность объекта'''
        return self._energy
    @Energy.setter
    def Energy(self, value:float):
        try:
            if value > self.TopTreshold:
                deltae = (self._energy + value) - self.TopTreshold
                biomtransform = self.EnergyCoeff + self.TransCoeff
                deltam = deltae / biomtransform
                self._energy = self.TopTreshold
                self.Biomass += deltam
                return
        except:
            print("Food.Energy – введённое значение не является числом")

class Animal(Food):
    """Животные. Базовый класс"""
    # Инициализация класса. Создание внутренних переменных
    def __init__(self):
        super().__init__()
        self._foodtype = 0 # 0 - травоядное, 1 - хищное , 2 - всеядное
        self._foodsize = 0 
        self._speed = 0.
        self._sleeptime = 0 # 0 - ночное, 1 - дневное, 2 - и то и другое
        self._animaltype = 0 # 0 - простейшее, 1 - плоские черви, 2 - круглые черви, 3 - кольчатые черви, 4 - кишечнополостные, 5 - членистоногие, 6 - моллюски, 7 - иглокожие, 8 - хордовые 
        self._rotteneattype = 0 # 0 - не ест гниль, 1 - ест только гниль, 2 - безразлично
        self._aim = np.zeros(2, float)
        self._stamina = random.randint(1, 11)
        self._aim_object = None
        self._eatenbiomass=0.
        self._eat_per_step = 10.
        self._digested_per_step = 0


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
            self._speed = float(value)
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
            if at >= 0 and at < 9:
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
            if ret >= 0 and ret < 3:
                self._rotteneattype = value
            else:
                print("Animal.RottenEatType не является допустимым значением")
        except:
            print("Animal.RottenEatType не является допустимым значением") 



    @property 
    def Stamina(self):
        return self._stamina
    @Stamina.setter
    def Stamina(self,value): 
        try:
            self._stamina=int(value)
        except:
            pass
            print()

    # Свойство Aim. Определяет координаты, на которое животное хочет переместиться животное
    @property
    def Aim(self):
        '''Определяет координаты,\n на которое животное хочет переместиться животное'''
        return self._aim
    @Aim.setter
    def Aim(self, value):
        self._aim = value

    # Свойство Stamina. Определяет выносливость объекта
    @property
    def Stamina(self):
        return self._stamina
    @Stamina.setter
    def Stamina(self, value):
        try:
            if value < 0:
                self._stamina = 0
                return
            if value > 10:
                self._stamina = 10
                return
            self._stamina = int(value)
        except:
            print("Animal.Stamina не является числом")

    # Свойство AimObject. Определяет объект, к которому стремится животное
    @property
    def AimObject(self):
        return self._aim_object
    @AimObject.setter
    def AimObject(self, value):
        self._aim_object = value


    @property
    def EatenBiomass(self):
        return self._eatenbiomass
    @EatenBiomass.setter
    def EatenBiomass(self, value): 
        self._eatenbiomass = value

    def Vector_Length(self, vector):
        return math.sqrt(vector[0]**2 + vector[1]**2) 

    @property
    def EatPerStep(self):
        """Количество биомассы, которое животное съедает за шаг."""
        return self._eat_per_step
    @EatPerStep.setter
    def EatPerStep(self, value:float):
        try:
            value = float(value)
            if value>0:
                self._eat_per_step = value
        except:
            print("Неправильно установлено Animal.EatPerStep") 

    #Свойство Digested_Per_Step.Определяет Количество биомассы,перевариваемой за шаг
    @property
    def Digested_Per_Step(self):
        return self.digested_per_step
    @Digested_Per_Step.setter
    def Digested_Per_Step(self, value:float):
        try:
            self.digested_per_step=float(value)
        except:
            pass

    

    # Метод NormalVector. Выдаёт единичный вектор от данного вектора
    def NormalVector(self, Vect):
        lenght = self.Vector_Length(Vect)
        NewVector = np.array([Vect[0]/lenght, Vect[1]/lenght])
        return NewVector
            
    # Метод Eat. Проверяет может ли животное съесть обект и в зависимости от результата изменяет энергию животного
    def Eat(self, food:Food):
        CanEat = False


        if not food in self.Parent.Elements:
            return

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
            if food.Biomass <= self.EatPerStep:
                self.EatenBiomass += food.Biomass
                self.Parent.Delete(food)
                food.kill()
            else:
                self.EatenBiomass += self.EatPerStep
                food.Biomass -= self.EatPerStep

    # Метод Move. Передвижение
    def Move(self, force):
        StartPos = self.Position
        if force == 2 and self.Stamina < 2:
            force = 1
        if force == 5 and self.Stamina < 8:
            if force == 2 and self.Stamina < 2:
                force = 1
            else:
                force = 2

        V = np.array([self.Aim[0] - self.Position[0], self.Aim[1] - self.Position[1]])
        V1 = self.NormalVector(V)
        if (self.Vector_Length(V) < self.Vector_Length(V1) * self.Speed * force):
            self.X += V[0]
            self.Y += V[1]
        else:
            self.X += V1[0] * self.Speed * force
            self.Y += V1[1] * self.Speed * force

        if force == 1:
            self.Stamina += 1
        if force == 2:
            self.Stamina -= 2
        if force == 5:
            self.Stamina -= 8

        #Parent.Ground[StartPos[0], StartPos[1]].remove(self)
        #Parent.Ground[Position[0], Position[1]].append(self)

    # Итерация действия у животного.
    def Step(self):
        super().Step()

        if abs(self.Aim[0] - self.Position[0]) < 0.5 and abs(self.Aim[1] -self.Position[1]) < 0.5:
            self.OnAim(self.AimObject)
            self.SetAim()
        self.Move(1)

    # Установка цели
    def SetAim(self):
        ''' Установка цели '''
        self.Aim = np.array([float(random.randint(0, self.Parent.Width)), float(random.randint(0, self.Parent.Height))]) 
        self.AimObject

    def Path(self,Other):
        dx=Other.X-self.X
        dy=Other.Y-self.Y
        return self.Vector_Length(np.array([dx,dy]))

    def OnAim(self, Aim):
        """Метод, вызываемый при достижении цели"""
        pass

#    def Aim_1_Atack(self, classes):
#        for name in classes:
#            m = Environment.Field.Alive
#            Aims = list(filter(lambda x: Path(x) < 10 and x.__class__.__name__ == name, self.Parent(m)))
#            AimsCount = len(Aims)
#            if AimsCount == 0:
#                self.SetAim()
#                return
#            if AimsCount == 1:
#                self.Aim = Aims[0].Position
#                return
#            if AimsCount < 4:
#                self.Aim = Aims[random.randint(0, AimsCount - 1)].Position
#                return
#            Aims.sort(key=lambda x: self.Path(x))
#            self.Aim = Aims[random.randint(0, 3)].Position
#            return self.Aim


class Plants(Food):
    """Базовый класс растений"""
    def _init_(self):
        super().__init__()
        self._amountofchllorophill = 0.0
        self._toxicity = False
        self._plant_type = 0

    # Количество хлорофила 0 - отсутствует, 1 - мало, 2 - среднее, 3 - много
    @property 
    def AmountOfChlorophill(self):
        """Определяет колтчество хлорофила"""
        return self._amountofchllorophill
    @AmountOfChlorophill.setter
    def AmountOfChlorophill(self, value):
        try:
            self._amountofchllorophill = int(value)
        except:
            print("Plants.AmOfChl не является целым числом")
                  
    # Токсичность 0 - нетоксично, 1 - малотоксичный (неприятно), 2 - среднетоксичный (болезнь) 3 - Смертельный 
    @property
    def Toxicity(self):
        """Определяет токсичность растения"""
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
        """Определяет тип растения"""
        return self._plant_type
    @PlantType.setter
    def PlantType(self,value):
        try:
            self._plant_type=int(value) 
        except:
            print("Plants.PlantType не является целым числом")
            print("Food.FreshTime не является целым числом") 

    def photosyntes(self, light):
        #if not bool(light):
        #    return
        """Добавляет определенное кол-во энергнии в зависимости от размера"""
        K=50
        E = K*self.AmountOfChlorophill
        if self._size == 0:
            self.Energy += E * 0.01
            return
        if self._size == 1:
            self.Energy += E*1
            return
        if self._size==2:
            self.Energy += E*10
            return
        if self._size==3:
            self.Energy += E*20
            return
        print("Error eating")

class Aim(Lifeless):
    def __init__(self):
        super().__init__()
        aim_img = pygame.image.load(pathlib.Path(InterfaceDir, "aim.png")).convert_alpha()
        self.image = aim_img
        self.rect = self.image.get_rect()
        self.rect.center = (self.X * 16 + 8, self.Y * 16 + 8)

    def update(self):
        self.rect.center = (self.X * 16 + 8, self.Y * 16 + 8)


