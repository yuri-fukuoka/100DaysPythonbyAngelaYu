import random


options = ["rock", "paper", "scissors"]


win_relations = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


player_choice = int(input("Choose 0 for rock, 1 for paper, and 2 for scissors: "))
player_choice = options[player_choice]


computer_choice = random.choice(options)


if player_choice == computer_choice:
    print("It's a draw!")
elif win_relations[player_choice] == computer_choice:
    print("You win!")
else:
    print("You lose!")





