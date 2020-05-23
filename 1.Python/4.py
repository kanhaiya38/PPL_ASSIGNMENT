"""
    4. Make a program that randomly chooses a number to guess
       and then the user will have a few chances to guess the number correctly.
       In each wrong attempt, the computer will give a hint that
       the number is greater or smaller than the one you have guessed.
"""

import random

random_num = random.randint(1, 100)
won = False

print("You have 5 chance to guess the number")

for _ in range(5):
    guess = int(input("Guess the number "))
    if guess < random_num:
        print("The number is greater than {}".format(guess))
    elif guess > random_num:
        print("The number is smaller than {}".format(guess))
    else:
        won = True
        break

if won:
    print("Congratulations!!! You won")
else:
    print("You lost, better luck next time. The number was {}".format(random_num))
