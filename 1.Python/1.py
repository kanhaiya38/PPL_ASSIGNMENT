"""
    1. Solve the puzzle with a Python program :
        A man is walking down the village road
        with a tiger, a goat and a bundle of grass.
        Soon he arrives at the river bank
        where there is one tiny boat that can carry him and another
        animal or grass at a time.
       Here is the problem: Left alone, the tiger will eat the goat.
        And similarly, the goat will eat the grass bundle.
        How is he going to take all three across the river safely?
"""

import random
sideone = ['Tiger', 'goat', 'grass']
sidetwo = []
present = True


def valid_check(side):
    if ('grass' in side) and ('goat' in side):
        return False
    elif ('goat' in side) and ('Tiger' in side):
        return False
    else:
        return True


count = 0
while(not(('goat' in sidetwo) and ('grass' in sidetwo) and ('Tiger' in sidetwo))):
    count += 1
    if(present == True):
        animal = random.choice(sideone)
        sideone.remove(animal)
        if(valid_check(sideone) == False):
            sideone.append(animal)
        else:
            sidetwo.append(animal)
            present = False

    else:
        if(valid_check(sidetwo) == False):
            animal = sidetwo.pop(0)
            sideone.append(animal)
        present = True

    print("side: ", end="")
    if present:
        print("sideone")
    else:
        print("sidetwo")
    print("sideone: ", sideone)
    print("sidetwo: ", sidetwo)
    print("*" * 20)
print(count)
