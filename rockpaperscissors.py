import random

rock = ["rock", "paper", "scissors"]
computer: str = random.choice(rock)
player = None

while player:
    player = input("rock paper scissors?: ")
    print("computer: %s" % computer)

    if (computer == "paper") and (player == "rock"):
        print("You lose, Paper covers Rock")
        continue
    elif (computer == "rock") and (player == "scissors"):
        print("You lose, rock break scissors")
        continue
    elif (computer == "scissors") and (player == "paper"):
        print("You lose, scissors cut paper")
        continue
    elif (player == "paper") and (computer == "rock"):
        print("You Win, paper covers rock.")
        continue
    elif (player == "rock") and (computer == "scissors"):
        print("You Win, rock break scissors")
        continue
    elif (player == "scissors") and (computer == "paper"):
        print("You Win, scissors cut paper")
        continue
    elif player == computer:
        print("draw, Try again")
        continue
