import Elements 

animal = Elements.Animal()
food = Elements.Food()
animal.Energy = 4.5
food.Energy = 3.4
animal.FoodType = 2
food.IsPlant = True
animal.FoodSize = 3
food.Size = 2
animal.Eat(food)
print(animal.Energy)

