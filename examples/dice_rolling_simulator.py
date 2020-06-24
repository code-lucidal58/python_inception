"""
Dice Rolling Simulator: Roll dice with numbers from 1 to 6 on its faces.
"""
from random import randint


def roll_dice():
    print("Rolling the dice...")
    print(randint(1, 6))


roll_dice()
rollAgain = True
while rollAgain:
    condition = True
    res = ''
    while condition:
        allowedChars = ['Y', 'y', 'N', 'n']
        res = input("Want to roll again? (y/n)")
        if len(res) == 1 and res in allowedChars:
            condition = False
    if res == 'Y' or res == 'y':
        roll_dice()
    else:
        print("Thank you! Have a Nice day! :D")
        rollAgain = False
