import pygame
import numpy as np
import Elements
import Environment
import random

# Функция создания и добавления Зверя
def CreateBeast(x,y,ax,ay):
    # Создание Зверя
    Beast = Elements.Beast()
    Beast.Position = np.array([x,y])
    Beast.Aim = np.array([ax,ay])
    Beast.Speed = 1
    Beast.Parent = Env
    Beast.Stamina = 10
    #Env.Ground[500,500].append(animal)
    Env.Elements.append(Beast)
    Env.Alive.append(Beast)

    # Добавление спрайтов в группу
    all_sprites.add(Beast)
    all_sprites.add(Beast._aim_sprite)

def CreateFox(x, y, ax, ay):
    # Создание Зверя
    Fox = Elements.Fox()
    Fox.Position = np.array([x, y])
    Fox.Aim = np.array([ax, ay])
    Fox.Speed = 2
    Fox.Parent = Env
    Fox.Stamina = 20
    Env.Elements.append(Fox)
    Env.Alive.append(Fox)

    # Добавление спрайта в группу
    all_sprites.add(Fox)
    all_sprites.add(Fox._aim_sprite)

# Функция, создающая траву
def CreateGrass():
    Grass = Elements.Grass()
    Grass.X = random.randint(0, Env.Width - 1)
    Grass.Y = random.randint(0, Env.Height - 1)
    Grass.Parent = Env
    Env.Elements.append(Grass)
    Env.Alive.append(Grass)

    # Добавление спрайтов в группу
    all_sprites.add(Grass)

# Визуализация
FPS = 15
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((1792, 896))
pygame.display.set_caption("Forest")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Создание среды
Env = Environment.Field()

# Создание объектов
for i in range(0, 100):
    CreateBeast(0, 0, 10, 10)
    CreateFox(0, 0, 9, 9)

for i in range(0, 400):
    CreateGrass()


running = True
while running:
    # Ограничение FPS
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Визуализация (сборка)
    screen.fill(0x00FF00)
    all_sprites.draw(screen)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    pass

pygame.quit()