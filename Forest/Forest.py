import pygame
import numpy as np
import Environment
import random
import Plants
import Animals
import ProgramInterface
import math
import Regions
import time


def CreateBeast(x: float, y: float, ax: float, ay: float):
    """Функция для создания абстрактного зверя для отладки"""
    # Создание Зверя
    Beast = Animals.Beast()
    Beast.Position = np.array([x, y])
    Beast.Aim = np.array([ax, ay])
    Beast.Speed = 1.
    Beast.EcoSystem = Env
    Beast.Stamina = 10
    Beast.Digested_Per_Step = 0.
    Beast.Biomass = 10.
    Beast.EnergyPerStep = 0.
    # Env.Ground[500,500].append(animal)
    Env.Elements.append(Beast)
    Env.Alive.append(Beast)

    # Добавление спрайтов в группу
    all_sprites.add(Beast)
    all_sprites.add(Beast._aim_sprite)
    animals_sprites.add(Beast)
    interface_sprites.add(Beast._aim_sprite)


def CreateFox(x: float, y: float, ax: float, ay: float):
    """Функция для создания песца"""
    Fox = Animals.Fox()
    Fox.Position = np.array([x, y])
    Fox.Aim = np.array([ax, ay])
    Fox.Speed = 1.
    Fox.EcoSystem = Env
    Fox.Stamina = 20
    Fox.Lower_Treshold = 2
    Fox.Digested_Per_Step = 0.
    Fox.Biomass = 10.
    Fox.EnergyPerStep = 0.
    Env.Elements.append(Fox)
    Env.Alive.append(Fox)

    # Добавление спрайта в группу
    all_sprites.add(Fox)
    all_sprites.add(Fox._aim_sprite)
    animals_sprites.add(Fox)
    interface_sprites.add(Fox._aim_sprite)


def CreateTurtle(x: float, y: float, ax: float, ay: float):
    """Функция для создания черепахи для отладки"""
    Turtle = Animals.Turtle()
    Turtle.Position = np.array([x, y])
    Turtle.Aim = np.array([ax, ay])
    Turtle.Speed = 0.5
    Turtle.EcoSystem = Env
    Turtle.Stamina = 3
    Turtle.TopTreshold = 44.
    Turtle.Digested_Per_Step = 1
    Turtle.Biomass = 10
    Turtle.EatenBiomass = 1
    Turtle.EatenBiomassTreshold = 50.
    Turtle.Eaten_Biomass_Lower_Treshold = 10.
    Turtle.EatPerStep = 10.
    Turtle.EnergyPerStep = 1.

    # Добавление спрайта в группу
    all_sprites.add(Turtle)
    all_sprites.add(Turtle._aim_sprite)
    animals_sprites.add(Turtle)
    interface_sprites.add(Turtle._aim_sprite)


def CreateChameleon(x: float, y: float, ax: float, ay: float):
    """Функция для создания хамелеона для отладки"""
    Chameleon = Animals.Chameleon()
    Chameleon.Position = np.array([x, y])
    Chameleon.Aim = np.array([ax, ay])
    Chameleon.Speed = 1.
    Chameleon.EcoSystem = Env
    Chameleon.Stamina = 5
    Chameleon.Digested_Per_Step = 0.
    Chameleon.Digested_Per_Step = 10
    Env.Elements.append(Chameleon)
    Env.Alive.append(Chameleon)

    # Добавление спрайта в группу
    all_sprites.add(Chameleon)
    all_sprites.add(Chameleon._aim_sprite)
    animals_sprites.add(Chameleon)
    interface_sprites.add(Chameleon._aim_sprite)


# Функция, создающая кролика из Террарии
def CreateBunny(x, y, ax, ay):
    # Создание кролика
    Bunny = Animals.Bunny()
    Bunny.Position = np.array([x, y])
    Bunny.Aim = np.array([ax, ay])
    Bunny.Speed = 2.5
    Bunny.EcoSystem = Env
    Bunny.Stamina = 11
    Bunny.Digested_Per_Step = 15.
    Env.Elements.append(Bunny)
    Env.Alive.append(Bunny)
    Bunny.Biomass = 25000.
    Bunny.EatenBiomass = 1
    Bunny.EatenBiomassTreshold = 50.
    Bunny.Eaten_Biomass_Lower_Treshold = 10.
    Bunny.EatPerStep = 10.
    Bunny.EnergyPerStep = 1.

    # Добавление спрайта в группу
    all_sprites.add(Bunny)
    all_sprites.add(Bunny._aim_sprite)
    animals_sprites.add(Bunny)
    interface_sprites.add(Bunny._aim_sprite)


def CreateWolf(x, y, ax, ay):
    # Создание волка
    Wolf = Animals.Wolf()
    Wolf.Position = np.array([x, y])
    Wolf.Aim = np.array([ax, ay])
    Wolf.Speed = 2.5
    Wolf.EcoSystem = Env
    Wolf.Stamina = 11
    Wolf.Digested_Per_Step = 15.
    Env.Elements.append(Wolf)
    Env.Alive.append(Wolf)
    Wolf.Biomass = 25000.
    Wolf.EatenBiomass = 1
    Wolf.EatenBiomassTreshold = 50.
    Wolf.Eaten_Biomass_Lower_Treshold = 10.
    Wolf.EatPerStep = 10.
    Wolf.EnergyPerStep = 1.

    # Добавление спрайта в группу
    all_sprites.add(Wolf)
    all_sprites.add(Wolf._aim_sprite)
    animals_sprites.add(Wolf)
    interface_sprites.add(Wolf._aim_sprite)


# Функция, создающая траву
def CreateGrass(Parent=None):
    """Функция для создания травы"""
    Grass = Plants.Grass()
    if Parent == None:
        Grass.X = random.randint(0, Env.Width - 1)
        Grass.Y = random.randint(0, Env.Height - 1)
    else:
        angle = random.randint(0, 360)
        angle = float(angle / 360 * 2 * math.pi)
        Grass.X = Parent.X + math.cos(angle)
        Grass.Y = Parent.Y + math.sin(angle)
    Grass.IsPlant = True
    Grass.EcoSystem = Env
    Grass.EnergyPerStep = 0.5
    Grass.AmountOfChlorophill = 2.
    Env.Elements.append(Grass)
    Env.Alive.append(Grass)
    Grass.TopTreshold = 23.
    Grass.Biomass = 500.
    Grass.Energy = 10.

    # Добавление спрайтов в группу
    all_sprites.add(Grass)
    plants_sprites.add(Grass)

def SetPause():
    global pause
    global Pause
    pause = not pause
    Pause.Show = pause

def CloseWindow():
    global running
    running = False
    print("Closing")


# Визуализация
FPS = 15
pygame.init()
#pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Forest")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
plants_sprites = pygame.sprite.Group()
animals_sprites = pygame.sprite.Group()
interface_sprites = pygame.sprite.Group()

# Создание среды
monitor_info = pygame.display.Info()
Env = Environment.Field(monitor_info)

# Создание объектов
for i in range(0, 10):
    CreateBeast(0., 0., 10., 10.)
    CreateFox(0., 0., 9., 9.)
    CreateTurtle(2., 3., 0., 0.)
    CreateBunny(2., 3., 3., 2.)
    CreateWolf(4., 4., 4., 4.)

for i in range(0, 40):
    CreateGrass()

# Создание окна интерфейса
Pause = ProgramInterface.PauseWindow()
Pause.Show = False
interface_sprites.add(Pause)
all_sprites.add(Pause)

StepsCountWindow = ProgramInterface.StepsWindow()
interface_sprites.add(StepsCountWindow)
all_sprites.add(StepsCountWindow)
StepsCountWindow.Count = 5326

Region = Regions.Region([23, 23], [100, 100])
interface_sprites.add(Region)
all_sprites.add(Region)

AliveCount = ProgramInterface.AliveCountWindow()
AliveCount.Show = True
interface_sprites.add(AliveCount)
all_sprites.add(AliveCount)

BiomassCount = ProgramInterface.BiomassCount()
interface_sprites.add(BiomassCount)
all_sprites.add(BiomassCount)

BiomassCountAnimal = ProgramInterface.BiomassCountAnimal()
interface_sprites.add(BiomassCountAnimal)
all_sprites.add(BiomassCountAnimal)

BiomassCountPlants = ProgramInterface.BiomassCountPlants()
interface_sprites.add(BiomassCountPlants)
all_sprites.add(BiomassCountPlants)

Buttons = ProgramInterface.Clickable()

Button = ProgramInterface.Button(np.array([300,10]), np.array([100,40]))
Button.Text = "Пауза"
Button.Click = SetPause
Buttons.add(Button)
interface_sprites.add(Button)
all_sprites.add(Button)

ExitButton = ProgramInterface.Button(np.array([monitor_info.current_w - 50, monitor_info.current_h - 50]), np.array([40,40]))
ExitButton.Text = "X"
ExitButton.Click = CloseWindow
Buttons.add(ExitButton)
interface_sprites.add(ExitButton)
all_sprites.add(ExitButton)

running = True
interface = True
pause = False

steps = 0

while running:
    StartTime = time.process_time_ns()/1000000
    # Ограничение FPS
    clock.tick(FPS)
    biomas = 0.
    anim_biomass = 0.
    plants_biomass = 0.
    all_animals = 0
    all_plants = 0
    wolves = 0
    rabbits = 0
    turtles = 0

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            CloseWindow()

        # Проверка нажатия кнопки
        if event.type == pygame.KEYDOWN:

            # Проверяем кнопку Esc для закрытия
            if event.key == pygame.K_ESCAPE:
                running = False

            # Проверяем кнопку I для отображения / скрытия интерфейсных элементов
            if event.key == pygame.K_i:
                interface = not interface

            # Проверяем кнопку P для паузы в симуляции
            if event.key == pygame.K_p:
                SetPause()

    #            if event.key == pygame.K_t:
    #                CreateTurtle(23., 32., 0., 0.)
    #            if event.key == pygame.K_f:
    #                CreateFox(32., 23., 0., 0.)
    #            if event.key == pygame.K_b:
    #                CreateBeast(40., 15., 0., 0.)

        if event.type == pygame.MOUSEBUTTONDOWN:
            Buttons.MouseDown(event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            Buttons.MouseUp(event.pos)

        if event.type == pygame.MOUSEMOTION:
            Buttons.MouseMove(event.pos)

    # Обновление

    if pause:
        interface_sprites.update()
    else:
        all_sprites.update()
        StepsCountWindow.Count += 1
        all_animals = list(filter(lambda x: x.IsPlant == False, Env.Alive))
        all_plants = list(filter(lambda x: x.IsPlant == True, Env.Alive))
        wolves = list(filter(lambda x: x.IsPlant == False and x.__class__.__name__ == "Wolf", Env.Alive))
        rabbits = list(filter(lambda x: x.IsPlant == False and x.__class__.__name__ == "Rabbit", Env.Alive))
        turtles = list(filter(lambda x: x.IsPlant == False and x.__class__.__name__ == "Turtle", Env.Alive))
        for x in Env.Alive:
            biomas += x.Biomass
            if str(type(x)) in ["<class 'Animals.Beast'>","<class 'Animals.Turtle'>","<class 'Animals.Fox'>","<class 'Animals.Wolf'>","<class 'Animals.Chameleon'>","<class 'Animals.Bunny'>"]:
                anim_biomass += x.Biomass
            if str(type(x)) == "<class 'Plants.Grass'>":
                plants_biomass+=x.Biomass
        BiomassCount.All_Bio_Count = biomas
        BiomassCountAnimal.Animal_Bio_Count = anim_biomass
        BiomassCountPlants.Plants_Bio_Count = plants_biomass

        AliveCount.AnimalsCount = len(all_animals)
        AliveCount.TurtlesCount = len(turtles)
        AliveCount.PlantsCount = len(all_plants)
        AliveCount.WolvesCount = len(wolves)
        AliveCount.RabbitsCount = len(rabbits)
        
    #CreateGrass()


    # Визуализация (сборка)
    screen.fill(0x00FF00)
    animals_sprites.draw(screen)
    plants_sprites.draw(screen)
    if interface:
        interface_sprites.draw(screen)
        

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    EndTime = time.process_time_ns() / 1000000
    DT = EndTime - StartTime
    print(DT, 1 / (DT / 1000))

pygame.quit()