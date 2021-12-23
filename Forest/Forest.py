import pygame
import numpy as np
import Elements
import Environment

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
CreateBeast(0,0,10,10)

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