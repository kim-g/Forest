import pygame
import numpy as np
import Environment
import random
import Plants
import Animals
import ProgramInterface
import math

def CreateBeast(x:float, y:float, ax:float, ay:float):
    """Функция для создания абстрактного зверя для отладки"""
    # Создание Зверя
    Beast = Animals.Beast()
    Beast.Position = np.array([x,y])
    Beast.Aim = np.array([ax,ay])
    Beast.Speed = 1.
    Beast.EcoSystem = Env
    Beast.Stamina = 10
    Beast.Digested_Per_Step = 0.
    Beast.Biomass = 10.
    Beast.EnergyPerStep = 5.
    #Env.Ground[500,500].append(animal)
    Env.Elements.append(Beast)
    Env.Alive.append(Beast)

    # Добавление спрайтов в группу
    all_sprites.add(Beast)
    all_sprites.add(Beast._aim_sprite)
    animals_sprites.add(Beast)
    interface_sprites.add(Beast._aim_sprite)

def CreateFox(x:float, y:float, ax:float, ay:float):
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
    Fox.EnergyPerStep = 100.
    Env.Elements.append(Fox)
    Env.Alive.append(Fox)

    # Добавление спрайта в группу
    all_sprites.add(Fox)
    all_sprites.add(Fox._aim_sprite)
    animals_sprites.add(Fox)
    interface_sprites.add(Fox._aim_sprite)

def CreateTurtle(x:float, y:float, ax:float, ay:float):
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

def CreateChameleon(x:float, y:float, ax:float, ay:float):
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


def CreateGrass(Parent = None):
    """Функция для создания травы"""
    Grass = Plants.Grass()
    if Parent == None:
        Grass.X = random.randint(0, Env.Width - 1)
        Grass.Y = random.randint(0, Env.Height - 1)
    else:
        angle = random.randint(0,360)
        angle = float(angle / 360 * 2 * math.pi)
        Grass.X = Parent.X + math.cos(angle)
        Grass.Y = Parent.Y + math.sin(angle)
    Grass.IsPlant = True
    Grass.EcoSystem = Env
    Grass.EnergyPerStep = 5.
    Grass.AmountOfChlorophill = 2
    Env.Elements.append(Grass)
    Env.Alive.append(Grass)
    Grass.TopTreshold = 23.
    Grass.Biomass = 100.
    Grass.Energy = 32.

    # Добавление спрайтов в группу
    all_sprites.add(Grass)
    plants_sprites.add(Grass)

# Визуализация
FPS = 15
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((0,0))
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

for i in range(0, 400):
    CreateGrass()


# Создание окна интерфейса
Pause = ProgramInterface.PauseWindow()
Pause.Show = False;
interface_sprites.add(Pause)
all_sprites.add(Pause)

running = True
interface = True
pause = False

while running:
    # Ограничение FPS
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

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
                pause = not pause
                Pause.Show = pause

#            if event.key == pygame.K_t:
#                CreateTurtle(23., 32., 0., 0.)
#            if event.key == pygame.K_f:
#                CreateFox(32., 23., 0., 0.)
#            if event.key == pygame.K_b:
#                CreateBeast(40., 15., 0., 0.)

    # Обновление
    if pause:
        interface_sprites.update()
    else:
        all_sprites.update()
    #CreateGrass()

    # Визуализация (сборка)
    screen.fill(0x00FF00)
    animals_sprites.draw(screen)
    plants_sprites.draw(screen)
    if interface:
        interface_sprites.draw(screen)

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    pass



pygame.quit()