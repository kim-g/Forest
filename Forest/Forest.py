import numpy as np
import Elements
import Environment

Env = Environment.Field()
animal = Elements.Animal()
animal.Position = np.array([500,500])
animal.Aim = np.array([505,497])
animal.Speed = 1
animal.Parent = Env
#Env.Ground[500,500].append(animal)
Env.Elements.append(animal)
Env.Alive.append(animal)

while input() != "e":
    for i in range (0, 10):
        animal.Step()