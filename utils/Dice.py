import random

def createDie(sides: int) -> list:
    die = []
    for i in range(int(sides)):
        die.append(i+1)
    return die
    
def roll(dice: list) -> int:
    if len(dice) == 1:
        return random.choice(dice[0])
    else:
        out = []
        for i in dice:
            out.append(random.choice(i))
        return out