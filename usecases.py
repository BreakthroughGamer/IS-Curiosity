#Making Dice
from utils import Dice

d6 = Dice.createDie(6)

print(d6)

d6s = [d6, d6, d6]

print(Dice.roll(d6s))
print(Dice.roll([d6]))

