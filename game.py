import random

print("Welcome to Rock-Paper-Scissors!")

game = ["rock", "paper", "scissors"]

random_num = random.randint(0, 2)

print(f"Computer chose: {game[random_num]}")


player = input("Choose rock, paper, or scissors: ")
print(f"You chose: {player}")
