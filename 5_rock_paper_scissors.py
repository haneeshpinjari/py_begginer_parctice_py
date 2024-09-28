import random

choices = [ "rock", "paper", "scissors"]
user_choice = input("Enter rock, paper and scissors: ").lower()
computer_choice = random.choice(choices)

if user_choice == 'rock':
    print(f"Both chose {user_choice}.It's a tie.")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == 'paper' and computer_choice == "rock"):
    print(f"you win! {user_choice} beats {computer_choice}")
else:
    print(f"you lose! {computer_choice} beats {user_choice}")