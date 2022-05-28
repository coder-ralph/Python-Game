# Python - Rock, Paper, Scissors Game
import random

name = input()
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\n You chose {user_action}, computer chose {computer_action} \n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie")
elif user_action == "rock":
    if computer_action == "scissors":
      print(f"Rock beats scissors! {name} wins!")
    else:
      print(f"Paper beats rock! {name} lose!")
elif user_action == "paper":
    if computer_action == "rock":
      print(f"Paper beat rock! {name} wins!")
    else:
      print(f"Scissors beats paper! {name} lose!")
elif user_action == "scissors":
    if computer_action == "paper":
      print(f"Scissors beats paper! {name} wins!")
    else:
      print(f"Rock beats scissors! {name} lose!")