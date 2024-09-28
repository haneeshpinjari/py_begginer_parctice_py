import random

def roll_dice():
    return random.randint(1, 6)

while True:
    roll = input("Roll the dice? (y/n): ").lower()
    if roll == 'y':
        print(f"rolled: {roll_dice()}")
    else:
        break