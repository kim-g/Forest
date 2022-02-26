import pygame
import numpy as np
import Environment
import Elements
import random
import Plants
import Animals
import math

# Функция создания и добавления Зверя
def CreateBeast(x,y,ax,ay):
    # Создание Зверя
    Beast = Animals.Beast()
    Beast.Position = np.array([x,y])
    Beast.Aim = np.array([ax,ay])
    Beast.Speed = 1.
    Beast.EcoSystem = Env
    Beast.Stamina = 10
    Beast.Digested_Per_Step = 0.
    Beast.Biomass = 10.
    #Env.Ground[500,500].append(animal)
    Env.Elements.append(Beast)
    Env.Alive.append(Beast)

    # Добавление спрайтов в группу
    all_sprites.add(Beast)
    all_sprites.add(Beast._aim_sprite)
    animals_sprites.add(Beast)
    interface_sprites.add(Beast._aim_sprite)

def CreateFox(x, y, ax, ay):
    # Создание Зверя
    Fox = Animals.Fox()
    Fox.Position = np.array([x, y])
    Fox.Aim = np.array([ax, ay])
    Fox.Speed = 1.
    Fox.EcoSystem = Env
    Fox.Stamina = 20
    Fox.Lower_Treshold = 2
    Fox.Digested_Per_Step = 0.
    Fox.Biomass = 10.
    Env.Elements.append(Fox)
    Env.Alive.append(Fox)

    # Добавление спрайта в группу
    all_sprites.add(Fox)
    all_sprites.add(Fox._aim_sprite)
    animals_sprites.add(Fox)
    interface_sprites.add(Fox._aim_sprite)

def CreateTurtle(x, y, ax, ay):
    # Создание Зверя
    Turtle = Animals.Turtle()
    Turtle.Position = np.array([x, y])
    Turtle.Aim = np.array([ax, ay])
    Turtle.Speed = 0.5
    Turtle.EcoSystem = Env
    Turtle.Stamina = 3
    Turtle.TopTreshold = 44.
    Turtle.Digested_Per_Step = 1.
    Turtle.Biomass = 10

    # Добавление спрайта в группу
    all_sprites.add(Turtle)
    all_sprites.add(Turtle._aim_sprite)
    animals_sprites.add(Turtle)
    interface_sprites.add(Turtle._aim_sprite)

def CreateChameleon(x, y, ax, ay):
    # Создание Зверя
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

# Функция, создающая траву
def CreateGrass(Parent = None):
    Grass = Plants.Grass()
    if Parent == None:
        Grass.X = random.randint(0, Env.Width - 1)
        Grass.Y = random.randint(0, Env.Height - 1)
    else:
        angle = random.randint(0,360)
        angle = angle / 360 * 2 * math.pi
        Grass.X = Parent.X + math.cos(angle)
        Grass.Y = Parent.Y + math.sin(angle)
    Grass.IsPlant = True
    Grass.EcoSystem = Env
    Grass.AmountOfChlorophill = 2
    Env.Elements.append(Grass)
    Env.Alive.append(Grass)
    Grass.TopTreshold = 23.
    Grass.Biomass = 35.

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
Env = Environment.Field(pygame.display.Info())

# Создание объектов
for i in range(0, 10):
    CreateBeast(0., 0., 10., 10.)
    CreateFox(0., 0., 9., 9.)
    CreateTurtle(2., 3., 0., 0.)

for i in range(0, 400):
    CreateGrass()


running = True
interface = True
while running:
    # Ограничение FPS
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_i:
                interface = not interface
#            if event.key == pygame.K_t:
#                CreateTurtle(23., 32., 0., 0.)
#            if event.key == pygame.K_f:
#                CreateFox(32., 23., 0., 0.)
#            if event.key == pygame.K_b:
#                CreateBeast(40., 15., 0., 0.)

    # Обновление
    all_sprites.update()
    Grass = list(filter(lambda x: x.__class__.__name__ == "Grass", Env.Alive))
    LenGrass = len(Grass)-1
    CreateGrass()

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

