# Automatic Dice Roller
# Written by Sean Lynch
from random import randint
print("Automatic Dice Roller")

def dice_roller():
      print(randint(1,6))
    
roll = input("press Enter to roll")
  
while roll == "":
      print("The value is: ")
      dice_roller()
      roll = input("press Enter to roll again, or 'x' then Enter to quit")
print("Goodbye!")
