import random
number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess the number from 1 to 10: "))
    if guess < number:
        print(f"Too Low!")
    elif guess > number:
        print(f"Too high!")
    else:
        print(f"Congratulations! you guess the number correct.")