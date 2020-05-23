"""
    2. The dice rolling simulator will imitate the experience of rolling a dice.
       It will generate a random number and the user can play again and again
       to get a number from the dice until the user decides to quit the program.
"""

import random

quit = False

while not quit:

    command = input("Enter y to roll a dice and n to quit")
    if command.lower() == 'y':
        print(random.randint(1, 6))

    elif command.lower() == "n":
        quit = True

    else:
        print("Not a valid command")
