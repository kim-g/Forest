from numpy import True_
import Elements 

<<<<<<< HEAD
unit1 = Elements.Food()
unit1.TimeOfEndLife = "tyuyiiu"
print(unit1.TimeOfEndLife)
print(Elements.Unit.__doc__)
unit1 = Elements.Plants() 
unit1.Energy = 100
unit1.AmountOfChlorophill = 2
unit1._size = 2
unit1.photosyntes(True)
print(unit1.Energy) 
=======
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
>>>>>>> origin/Denis
