from numpy import True_
import Elements 

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